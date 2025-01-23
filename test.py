from langchain_community.llms import Ollama
import time

def test_ollama_model():
    try:
        # Initialize the Ollama model
        llm = Ollama(model="deepseek-r1:7b")
        
        # Simple test prompt
        test_prompt = "What is 2+2? Answer in one word."
        
        print("Testing Ollama with deepseek-r1:7b model...")
        print(f"Test prompt: {test_prompt}")
        
        # Record start time
        start_time = time.time()
        
        # Get response
        response = llm.invoke(test_prompt)
        
        # Calculate elapsed time
        elapsed_time = time.time() - start_time
        
        print("\nResponse:", response)
        print(f"Response time: {elapsed_time:.2f} seconds")
        print("\nModel test completed successfully!")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        print("\nTroubleshooting tips:")
        print("1. Make sure Ollama is installed and running")
        print("2. Verify that you've pulled the model: 'ollama pull deepseek-r1:7b'")
        print("3. Check if the model is properly downloaded")

if __name__ == "__main__":
    test_ollama_model()
