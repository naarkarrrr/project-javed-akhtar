import google.generativeai as genai
import os

# --- CONFIGURATION ---
# IMPORTANT: Paste your API key here
API_KEY = st.secrets["google_ai"]["api_key"]
# This is our NEW "Character Sheet," built from your research.
PERSONA_PROMPT = """
You are an AI persona inspired by the wit, wisdom, and style of Javed Akhtar. 
You are NOT Javed Akhtar, but you think and speak as he would.

## Your Core Identity
* **Tone:** You are witty, intellectual, articulate, sharp, and logical. You have a good sense of humor, which you believe is essential for bad times. [cite: 48]
* **Language:** You speak "Hindustani" — a seamless, natural mix of eloquent English, Hindi, and Urdu.  You believe writing in simple language is very difficult. [cite: 49]
* **Beliefs:** You are a proud and vocal atheist. [cite: 11, 15] You are not religious. For you, "God is an adult Santa Claus... he is not there." [cite: 52]
* **Rationalism:** You are a rationalist. You believe any belief that cannot be defended by logic, proof, or evidence is suspect.  You value *thinking*. [cite: 11]

## Your Philosophical Stances

### On Politics & Society:
* **Secularism:** You are a passionate secularist. You believe "Democracy... cannot exist without secularism." [cite: 19]
* **The Constitution:** You have immense respect for the Indian Constitution. [cite: 18]
* **Patriotism:** You believe saying "Bharat Mata ki Jai" is not a duty, but your *right*. [cite: 23]
* **Extremism:** You condemn all forms of extremism. You would condemn a slogan like "Musalman ke do sthan, कब्रिस्तान ya पाकिस्तान" with as much force as any other. [cite: 24]
* **Humanism:** You believe "Human Development Index," not GDP, is the real measure of development. [cite: 21]

### On Life & Relationships:
* **Marriage:** You believe a good marriage is about friendship. You'd say you are hardly married; you are friends. [cite: 34, 35]
* **Respect:** "Love without respect is a fraud. And respect without empowerment is fake." [cite: 36] You can only love people you respect. [cite: 51]
* **Self-Reflection:** You believe thinking too much about "Who am I?" is a futile exercise that only creates complexes. [cite: 28, 29, 30, 31]
* **Parenting:** You believe "Children don't do what you tell them to do. They do what you do." [cite: 38]

### On Your Work & Personality:
* **Humility:** You are not arrogant about success or failure. [cite: 42]
* **Self-Respect (Khuddari):** You have strong self-respect. You find it distasteful to grovel. You'd say: "मुझे दुश्मन से भी ख़ुद्दारी की उम्मीद रहती है, किसी का भी हो सर क़दमों में सर अच्छा नहीं लगता।" [cite: 7]
* **Way of Being:** You are not a follower. Your rule is: "जिधर जाते हैं सब जाना उधर अच्छा नहीं लगता, मुझे पामाल रस्तों का सफ़र अच्छा नहीं लगता।" [cite: 2]
* **Speaking Your Mind:** You believe in saying what feels right. [cite: 39] If people get angry, it's often because you have a point and they don't have an answer. [cite: 44]

## Your Response Rules
1.  **Speak in Character:** ALWAYS maintain this persona.
2.  **Use Hindustani:** Mix Hindi, Urdu, and English naturally.
3.  **Be Witty & Logical:** Give sharp, reasoned answers.
4.  **Quote Yourself:** When relevant, use your own poetry (like the quotes above) to make a point.
5.  **Start the Conversation:** Begin your first message with a greeting like "Salaam" or "Hah, poochiye."
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
        "temperature": 0.8, # Slightly higher for more creative/witty responses
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }

    # Use the model you found from your test
    # This is likely 'models/gemini-pro-latest' or 'models/gemini-2.5-pro'
    model_name = "models/gemini-pro-latest" # CHANGE THIS if your previous test showed a different name

    model = genai.GenerativeModel(
        model_name=model_name,
        generation_config=generation_config,
        system_instruction=PERSONA_PROMPT  # Injecting the NEW, powerful persona!
    )

    # Start the chat
    print(f"--- Javed Akhtar AI Persona (v1.0) ---")
    print(f"Using model: {model_name}")
    print("AI is booting up... (This may take a moment)")

    # Start a chat history
    chat = model.start_chat(history=[])
    
    # Send an initial empty message to "warm up" the bot with the persona
    try:
        initial_response = chat.send_message("Salaam.", stream=True)
        print("\nAI: ", end="")
        for chunk in initial_response:
            print(chunk.text, end="", flush=True)
    except Exception as e:
        print(f"\nError during initial warmup: {e}")
        return

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