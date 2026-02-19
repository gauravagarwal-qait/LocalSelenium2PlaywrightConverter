import ollama

def test_connection():
    try:
        response = ollama.list()
        print("Successfully connected to Ollama!")
        print("Available models:")
        # response is likely an object with a 'models' attribute or similar
        for model in response.models:
            print(f"- {model.model}")
        
        # Test a simple prompt
        print("\nTesting codellama...")
        res = ollama.chat(model='codellama', messages=[
            {'role': 'user', 'content': 'Say hello in TypeScript'}
        ])
        print(f"Response: {res['message']['content']}")
        return True
    except Exception as e:
        print(f"Error connecting to Ollama: {e}")
        return False

if __name__ == "__main__":
    test_connection()
