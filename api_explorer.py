"""
AI API Explorer
This file contains code to test and explore various AI APIs
"""

# ============================================
# Google Gemini AI (NEW google.genai) Example
# ============================================
try:
    import google.genai as genai
    
    # Configure API key (set your API key here)
    API_KEY = "YOUR_GOOGLE_API_KEY_HERE"
    client = genai.Client(api_key=API_KEY)
    
    # Example: Generate text using Gemini 2.0 Flash
    def generate_text_gemini(prompt):
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text
    
    # List available models
    def list_gemini_models():
        models = client.models.list()
        return [model.name for model in models]
    
    # Test
    result = generate_text_gemini("What is machine learning?")
    print(result)
    
except ImportError:
    print("Google Gemini AI not installed. Install with: pip install google-genai")
except Exception as e:
    print(f"Error with Google Gemini API: {e}")


# ============================================
# OpenAI API Example
# ============================================
try:
    from openai import OpenAI
    
    # Configure API key
    API_KEY = "sk-navy-WFgddbNe5X4GjLH0IsGJJiRtOclpOmAysuTthKU7DoA"
    client = OpenAI(api_key=API_KEY)
    
    def openai_chat(message):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": message}
            ]
        )
        return response.choices[0].message.content
    
    # Test
    result = openai_chat("Explain neural networks")
    print(result)
    
except ImportError:
    print("OpenAI not installed. Install with: pip install openai")
except Exception as e:
    print(f"Error with OpenAI: {e}")


# ============================================
# Hugging Face API Example
# ============================================
try:
    from huggingface_hub import InferenceClient
    
    # Configure API key (Note: This appears to be an OpenAI key, not a Hugging Face key)
    HF_API_KEY = "YOUR_HUGGINGFACE_API_KEY_HERE"
    client = InferenceClient(token=HF_API_KEY)
    
    def huggingface_inference(prompt):
        response = client.text_generation(
            prompt,
            max_new_tokens=100
        )
        return response
    
    # Test
    result = huggingface_inference("Hello, how are you?")
    print(result)
    
except ImportError:
    print("Hugging Face not installed. Install with: pip install huggingface-hub")
except Exception as e:
    print(f"Error with Hugging Face: {e}")


# ============================================
# API Testing Template
# ============================================
class APITester:
    """Template class for testing different APIs"""
    
    def __init__(self, api_name, api_key):
        self.api_name = api_name
        self.api_key = api_key
    
    def test_connection(self):
        """Test if API connection is working"""
        print(f"Testing {self.api_name} connection...")
        # Implementation here
        pass
    
    def test_model_list(self):
        """List available models"""
        print(f"Available models for {self.api_name}:")
        # Implementation here
        pass
    
    def test_inference(self, prompt):
        """Test inference with a prompt"""
        print(f"Testing inference on {self.api_name}...")
        print(f"Prompt: {prompt}")
        # Implementation here
        pass


if __name__ == "__main__":
    print("=" * 50)
    print("AI API Explorer")
    print("=" * 50)
    print("\nInstructions:")
    print("1. Replace YOUR_API_KEY_HERE with your actual API key")
    print("2. Uncomment the test code in each section")
    print("3. Run this file to explore the API")
    print("\n" + "=" * 50)
