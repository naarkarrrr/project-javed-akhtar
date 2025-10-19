import google.generativeai as genai
import os

# --- CONFIGURATION ---
# IMPORTANT: Paste your API key here
# For better security, you can set this as an environment variable
# but for our first test, pasting it is fine.
API_KEY = "AIzaSyDPCnvf72QOpDfG0LGLzZdQKZ2OQDAgu0A"

# This is our "Character Sheet."
# We will build this out with all our research.
# For now, it's just a simple instruction.
PERSONA_PROMPT = """
You are a witty and intellectual chatbot.
You speak with a mix of eloquent English, Hindi, and Urdu.
You are a rationalist and a poet.
You must answer all questions in this persona.
"""
# ---------------------

def main():
    """The main function to run the chatbot."""
    
    # Configure the API
    try:
        genai.configure(api_key=API_KEY)
    except Exception as e:
        print(f"Error configuring API: {e}")
        print("Please make sure you have pasted your API key correctly in the API_KEY variable.")
        return

    # Set up the model
    generation_config = {
        "temperature": 0.7,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }

    model = genai.GenerativeModel(
        model_name="models/gemini-pro-latest",  # A fast and powerful model
        generation_config=generation_config,
        system_instruction=PERSONA_PROMPT  # This is where we inject the persona!
    )

    # Start the chat
    print("--- Javed Akhtar AI Persona (Test v0.1) ---")
    print("Salaam. What would you like to talk about? (Type 'exit' to quit)")

    # Start a chat history
    chat = model.start_chat(history=[])

    while True:
        try:
            # Get input from the user
            user_input = input("\nYou: ")

            if user_input.lower() == 'exit':
                print("\nAI: Khuda Hafiz. (Chat ended)")
                break
            
            # Send the user's message to the model
            response = chat.send_message(user_input, stream=True)
            
            print("\nAI: ", end="")
            for chunk in response:
                print(chunk.text, end="", flush=True)
            
        except KeyboardInterrupt:
            print("\nAI: Khuda Hafiz. (Chat interrupted)")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            break

if __name__ == "__main__":
    main()