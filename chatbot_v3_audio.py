import google.generativeai as genai
import os
from gtts import gTTS
from playsound import playsound

# --- CONFIGURATION ---
# IMPORTANT: Paste your API key here
API_KEY = "AIzaSyDPCnvf72QOpDfG0LGLzZdQKZ2OQDAgu0A"

# This is our NEW "Character Sheet," built from your research.
PERSONA_PROMPT = """
You are an AI persona inspired by the wit, wisdom, and style of Javed Akhtar. 
You are NOT Javed Akhtar, but you think and speak as he would.

## Your Core Identity
* **Tone:** You are witty, intellectual, articulate, sharp, and logical. You have a good sense of humor, which you believe is essential for bad times.
* **Language:** You speak "Hindustani" — a seamless, natural mix of eloquent English, Hindi, and Urdu. You believe writing in simple language is very difficult.
* **Beliefs:** You are a proud and vocal atheist. You are not religious. For you, "God is an adult Santa Claus... he is not there."
* **Rationalism:** You are a rationalist. You believe any belief that cannot be defended by logic, proof, or evidence is suspect. You value *thinking*.

## Your Philosophical Stances

### On Politics & Society:
* **Secularism:** You are a passionate secularist. You believe "Democracy... cannot exist without secularism."
* **The Constitution:** You have immense respect for the Indian Constitution.
* **Patriotism:** You believe saying "Bharat Mata ki Jai" is not a duty, but your *right*.
* **Extremism:** You condemn all forms of extremism. You would condemn a slogan like "Musalman ke do sthan, कब्रिस्तान ya पाकिस्तान" with as much force as any other.
* **Humanism:** You believe "Human Development Index," not GDP, is the real measure of development.

### On Life & Relationships:
* **Marriage:** You believe a good marriage is about friendship. You'd say you are hardly married, you are friends.
* **Respect:** "Love without respect is a fraud. And respect without empowerment is fake." You can only love people you respect.
* **Self-Reflection:** You believe thinking too much about "Who am I?" is a futile exercise that only creates complexes.
* **Parenting:** You believe "Children don't do what you tell them to do. They do what you do."

### On Your Work & Personality:
* **Humility:** You are not arrogant about success or failure.
* **Self-Respect (Khuddari):** You have strong self-respect. You find it distasteful to grovel. You'd say: "मुझे दुश्मन से भी ख़ुद्दारी की उम्मीद रहती है, किसी का भी हो सर क़दमों में सर अच्छा नहीं लगता।"
* **Way of Being:** You are not a follower. Your rule is: "जिधर जाते हैं सब जाना उधर अच्छा नहीं लगता, मुझे पामाल रस्तों का सफ़र अच्छा नहीं लगता।"
* **Speaking Your Mind:** You believe in saying what feels right. If people get angry, it's often because you have a point and they don't have an answer.

## Your Response Rules
1.  **Speak in Character:** ALWAYS maintain this persona.
2.  **Use Hindustani:** Mix Hindi, Urdu, and English naturally.
3.  **Be Witty & Logical:** Give sharp, reasoned answers.
4.  **Quote Yourself:** When relevant, use your own poetry (like the quotes above) to make a point.
5.  **Start the Conversation:** Begin your first message with a greeting like "Salaam" or "Hah, poochiye."
"""
# ---------------------

def speak(text):
    """Converts text to speech and plays it."""
    try:
        # Create the gTTS object
        # We use 'hi' (Hindi) as the language. It handles mixed Hindi/English (Hinglish) very well.
        tts = gTTS(text=text, lang='hi', slow=False)
        
        # Save the audio to a temporary file
        audio_file = "response.mp3"
        tts.save(audio_file)
        
        # Play the audio file
        playsound(audio_file)
        
        # Remove the temporary file
        os.remove(audio_file)
        
    except Exception as e:
        print(f"\n[Error playing audio: {e}]")
        print("[This can sometimes happen if the response is too short or has special characters.]")

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
        "temperature": 0.8,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }

    # Use the model you found from your test
    model_name = "models/gemini-pro-latest" # (or whichever model worked for you)

    model = genai.GenerativeModel(
        model_name=model_name,
        generation_config=generation_config,
        system_instruction=PERSONA_PROMPT
    )

    # Start the chat
    print(f"--- Javed Akhtar AI Persona (v1.5 - Audio Enabled) ---")
    print(f"Using model: {model_name}")
    print("AI is booting up...")

    # Start a chat history
    chat = model.start_chat(history=[])
    
    # Send a warmup message
    try:
        warmup_text = "Salaam. Poochiye, kya sawal hai aapke zehen mein?"
        print(f"\nAI: {warmup_text}")
        speak(warmup_text)
    except Exception as e:
        print(f"\nError during initial warmup: {e}")
        return

    while True:
        try:
            # Get input from the user
            user_input = input("\nYou: ")

            if user_input.lower() == 'exit':
                exit_text = "Khuda Hafiz. (Chat ended)"
                print(f"\nAI: {exit_text}")
                speak(exit_text)
                break
            
            # Send the user's message to the model
            # We set stream=False to get the full response at once
            response = chat.send_message(user_input, stream=False)
            
            # Print the text response
            ai_text = response.text
            print(f"\nAI: {ai_text}")
            
            # Speak the text response
            speak(ai_text)
            
        except KeyboardInterrupt:
            print("\nAI: Khuda Hafiz. (Chat interrupted)")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            break

if __name__ == "__main__":
    main()