import streamlit as st
import ollama
import os
import time

# --- Config ---
st.set_page_config(page_title="Selenium to Playwright Converter", layout="wide", page_icon="🚀")

# --- UI Aesthetics (B.L.A.S.T Stylize Phase) ---
css = """
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=JetBrains+Mono&display=swap" rel="stylesheet">
<style>
    .main {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #f8fafc;
        font-family: 'Inter', sans-serif;
    }
    h1, h2, h3 {
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        letter-spacing: -0.02em;
        background: linear-gradient(90deg, #38bdf8, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    div.stTextArea textarea {
        background-color: rgba(30, 41, 59, 0.7) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        color: #e2e8f0 !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 14px !important;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    div.stTextArea textarea:focus {
        border-color: #38bdf8 !important;
        box-shadow: 0 0 15px rgba(56, 189, 248, 0.2);
    }
    .stButton>button {
        background: linear-gradient(90deg, #0ea5e9, #6366f1);
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.75rem 1.5rem !important;
        font-weight: 600 !important;
        font-size: 16px !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        transition: transform 0.2s, box-shadow 0.2s;
        width: 100%;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        background: linear-gradient(90deg, #0284c7, #4f46e5);
    }
    .footer {
        text-align: center;
        padding: 2rem;
        font-size: 0.8rem;
        color: #94a3b8;
        letter-spacing: 0.1em;
    }
</style>
"""
st.html(css.strip())

# --- Sidebar for Settings ---
with st.sidebar:
    st.header("⚙️ Configuration")
    model_choice = st.selectbox("LLM Model", ["codellama:latest", "llama3.2:latest"], index=0)
    save_dir = st.text_input("Output Directory", "converted_tests")
    st.info("Ensure Ollama is running in the background.")
    if st.button("🔄 Clear Session"):
        st.session_state.converted_code = ""
        st.session_state.status = "Idle"
        st.rerun()

# --- Main App ---
st.title("B.L.A.S.T. Selenium Converter")
st.markdown("Transform legacy Selenium Java suites into blazing-fast Playwright TypeScript.")

col1, col2 = st.columns(2)

if 'converted_code' not in st.session_state:
    st.session_state.converted_code = ""
if 'status' not in st.session_state:
    st.session_state.status = "Idle"

with col1:
    st.subheader("Source: Selenium Java")
    java_code = st.text_area("Paste code here...", height=500, placeholder="public class LoginPage { ... }", key="java_input")

with col2:
    st.subheader("Target: Playwright TS")
    # Placeholder for streaming output
    output_placeholder = st.empty()
    if st.session_state.converted_code:
        output_placeholder.code(st.session_state.converted_code, language="typescript")
    else:
        output_placeholder.info("Resulting code will appear here after execution...")

if st.button("⚡ EXECUTE CONVERSION"):
    if not java_code.strip():
        st.warning("⚠️ Please provide source code to begin.")
    else:
        status_box = st.empty()
        progress_bar = st.progress(0)
        
        try:
            # 1. Loading SOP
            status_box.info("🔍 Loading Conversion Artifacts...")
            progress_bar.progress(10)
            
            with open('architecture/conversion_sop.md', 'r', encoding='utf-8') as f:
                sop_content = f.read()
            
            # 2. Reasoning Layer
            status_box.info(f"🧠 Reasoning with {model_choice} (Streaming)...")
            progress_bar.progress(30)
            
            system_prompt = f"""
            You are the B.L.A.S.T. Project Navigator. 
            MISSION: Convert Selenium Java to Playwright TS.
            
            MAPPING SOP:
            {sop_content}
            
            STRICT OUTPUT RULES:
            1. Output ONLY the converted TypeScript code.
            2. NO markdown code blocks (```). NO introductory/concluding text.
            3. Use async/await and Playwright locator patterns.
            4. Keep comments brief.
            """
            
            # Start conversion
            stream = ollama.chat(
                model=model_choice, 
                messages=[
                    {'role': 'system', 'content': system_prompt},
                    {'role': 'user', 'content': f"CONVERT TO PLAYWRIGHT TS (CODE ONLY):\n\n{java_code}"}
                ],
                stream=True
            )
            
            full_response = ""
            for chunk in stream:
                content = chunk['message']['content']
                full_response += content
                # Continuous update in the right window
                output_placeholder.code(full_response, language="typescript")
            
            # 3. Finalization
            if full_response.strip():
                status_box.success("✅ Conversion Complete!")
                progress_bar.progress(100)
                
                # Save to session and file
                st.session_state.converted_code = full_response.strip()
                
                if not os.path.exists(save_dir):
                    os.makedirs(save_dir)
                
                filename = f"converted_{int(time.time())}.spec.ts"
                full_path = os.path.join(save_dir, filename)
                with open(full_path, "w", encoding='utf-8') as f:
                    f.write(st.session_state.converted_code)
                
                st.toast(f"Saved to {full_path}")
                # Log raw for Layer 3
                if not os.path.exists(".tmp"):
                    os.makedirs(".tmp")
                with open(".tmp/last_conversion.log", "w", encoding="utf-8") as f:
                    f.write(full_response)
            else:
                st.error("❌ Model returned an empty response.")

        except Exception as e:
            st.error(f"❌ ARCHITECT ERROR: {e}")
            st.session_state.status = "Failed"

# --- Footer ---
footer_html = """
<div class="footer">
    POWERED BY B.L.A.S.T. PROTOCOL & ANTIGRAVITY • DETERMINISTIC AUTOMATION • 2026
</div>
"""
st.html(footer_html.strip())
