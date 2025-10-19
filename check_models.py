import google.generativeai as genai

# --- PASTE YOUR API KEY HERE ---
API_KEY = "AIzaSyDPCnvf72QOpDfG0LGLzZdQKZ2OQDAgu0A"
# -------------------------------

try:
    genai.configure(api_key=API_KEY)
    print("--- Available Models for your API Key ---")
    
    # List all models
    for model in genai.list_models():
        # Check if the model supports the 'generateContent' method
        if 'generateContent' in model.supported_generation_methods:
            print(f"Model name: {model.name}")
            print("  Supported methods:", model.supported_generation_methods)
            print("-" * 20)
            
    print("\n--- Recommendation ---")
    print("Find a model name above (like 'gemini-pro') and paste it into your chatbot.py file.")

except Exception as e:
    print(f"An error occurred: {e}")
    print("Please double-check that your API_KEY is correct.")