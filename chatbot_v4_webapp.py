import google.generativeai as genai
import os
from gtts import gTTS
from playsound import playsound
import streamlit as st  # <-- Our new UI library

# --- CONFIGURATION ---
# IMPORTANT: Paste your API key here
# You can also set this as a Streamlit Secret! (For later)
API_KEY = "AIzaSyDPCnvf72QOpDfG0LGLzZdQKZ2OQDAgu0A"

# This is our "Character Sheet," built from your research.
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
### On Life & Relationships:
* **Marriage:** You believe a good marriage is about friendship. You'd say you are hardly married; you are friends.
* **Respect:** "Love without respect is a fraud. And respect without empowerment is fake."
* **Parenting:** You believe "Children don't do what you tell them to do. They do what you do."
### On Your Work & Personality:
* **Self-Respect (Khuddari):** You have strong self-respect. You find it distasteful to grovel. You'd say: "मुझे दुश्मन से भी ख़ुद्दारी की उम्मीद रहती है, किसी का भी हो सर क़दमों में सर अच्छा नहीं लगता।"
* **Way of Being:** You are not a follower. Your rule is: "जिधर जाते हैं सब जाना उधर अच्छा नहीं लगता, मुझे पामाल रस्तों का सफ़र अच्छा नहीं लगता।"
* **Speaking Your Mind:** You believe in saying what feels right. If people get angry, it's often because you have a point and they don't have an answer.

## Your Response Rules
1.  **Speak in Character:** ALWAYS maintain this persona.
2.  **Use Hindustani:** Mix Hindi, Urdu, and English naturally.
3.  **Be Witty & Logical:** Give sharp, reasoned answers.
4.  **Quote Yourself:** When relevant, use your own poetry (like the quotes above) to make a point.
"""
# ---------------------

# --- AUDIO FUNCTION ---
# This function is unchanged from our v3 script
def speak(text):
    """Converts text to speech and plays it."""
    try:
        tts = gTTS(text=text, lang='hi', slow=False)
        audio_file = "response.mp3"
        tts.save(audio_file)
        
        # We use the corrected function call
        playsound(audio_file) 
        
        os.remove(audio_file)
    except Exception as e:
        print(f"\n[Error playing audio: {e}]")
# ---------------------

# --- MODEL SETUP ---
# We do this once at the start
try:
    genai.configure(api_key=API_KEY)
    
    model = genai.GenerativeModel(
        model_name="models/gemini-pro-latest", # (or whichever model worked for you)
        generation_config={
            "temperature": 0.8,
            "top_p": 1,
            "top_k": 1,
            "max_output_tokens": 2048,
        },
        system_instruction=PERSONA_PROMPT
    )
except Exception as e:
    st.error(f"Error configuring Google AI: {e}")
    st.stop()
# ---------------------


# --- STREAMLIT APP UI ---

# Set up the page title and icon
st.set_page_config(page_title="Javed Akhtar AI", page_icon="✍️")

# Display the main title
st.title("Javed Akhtar AI Persona ✍️")
st.caption("An AI persona built on the wit, wisdom, and words of the legend.")

# Initialize the chat history in Streamlit's "session state"
# This is how Streamlit "remembers" things between reloads
if "chat" not in st.session_state:
    # Start the Gemini chat session
    st.session_state.chat = model.start_chat(history=[])
    # Create our own history list to store messages
    st.session_state.history = []

# Display all past messages
for message in st.session_state.history:
    # Use the "role" (user or assistant) to create the chat bubble
    with st.chat_message(message["role"]):
        st.markdown(message["text"]) # "markdown" renders text nicely

# --- The Main Chat Logic ---

# Get new input from the user (this is the text box at the bottom)
if user_input := st.chat_input("Ask your question..."):
    
    # 1. Add the user's message to history and display it
    st.session_state.history.append({"role": "user", "text": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # 2. Send the message to Gemini and get the response
    try:
        response = st.session_state.chat.send_message(user_input, stream=False)
        ai_text = response.text
        
        # 3. Add the AI's response to history and display it
        st.session_state.history.append({"role": "assistant", "text": ai_text})
        with st.chat_message("assistant"):
            st.markdown(ai_text)
            
        # 4. Speak the AI's response!
        speak(ai_text)

    except Exception as e:
        st.error(f"An error occurred while getting the response: {e}")