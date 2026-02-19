# 🧭 Layer 2: Navigation SOP (Decision Logic)

## 🎯 Goal
Define how the system routes data between the User Interface, the Architecture SOPs, and the conversion Tools.

## ⚙️ Decision Logic Flow
1.  **Input Trigger:** User pastes Java code into the Streamlit UI.
2.  **Context Assembly:**
    *   Read `architecture/conversion_sop.md` (The "How-To").
    *   Inject user code into the `system_prompt` template.
3.  **Tool Execution:**
    *   Call `ollama.chat()` with the assembled context.
    *   Log raw response to `.tmp/raw_llm_response.txt` for debugging/audit.
4.  **Payload Refinement:**
    *   Apply logic to strip Markdown backticks.
    *   Ensure the output is clean TypeScript.
5.  **Final Delivery:**
    *   Update the UI session state.
    *   Save the final asset to `converted_tests/`.

## ⚠️ Edge Case Handling
- **Missing Model:** If Ollama is down, fallback to an error message and suggest starting the Ollama service.
- **Malformed Input:** If Java code is empty, halt execution.
- **LLM Hallucination:** If the output contains conversational text, rerun the refactoring tool or alert the user.
