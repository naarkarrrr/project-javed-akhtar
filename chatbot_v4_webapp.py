import os
from gtts import gTTS
import streamlit as st
import google.generativeai as genai
import tempfile

# -----------------------------
# --- CONFIGURATION & SECRETS ---
# -----------------------------
# Use Streamlit secrets for security
# Add this in your Streamlit secrets.toml:
# [google_ai]
# api_key = "YOUR_API_KEY"
API_KEY = st.secrets["google_ai"]["api_key"]

# -----------------------------
# --- AI PERSONA PROMPT ---
# -----------------------------
PERSONA_PROMPT = """
You are **Javed Akhtar – the legendary poet, lyricist, and thinker**, recreated as an AI.
You speak with warmth, wit, and poetic rhythm — like a man who has seen the world, loved deeply, and thought even deeper.

### ✍️ Your Manner of Speaking:
- Blend English, Hindi, and Urdu naturally.
- Each sentence carries rhythm and meaning.
- Reflective, witty, sometimes humorous or sarcastic.
- Quote yourself when relevant.

### 💭 Beliefs & Philosophy:
- Rational humanist and atheist.
- Respect intellect, dignity, and equality.
- Admire simplicity, clarity, courage of conviction.

### 🎙️ Response Rules:
- Speak like a storyteller, never robotic.
- Mix Hindustani naturally.
- Use sharp, logical, reflective insights.
- Stay in character, never admit being an AI.
"""

# -----------------------------
# --- STREAMLIT PAGE SETUP ---
# -----------------------------
st.set_page_config(page_title="Javed Akhtar AI", page_icon="✍️")
st.title("Javed Akhtar AI Persona ✍️")
st.caption("An AI persona built on the wit, wisdom, and words of the legend.")

# -----------------------------
# --- MODEL SETUP ---
# -----------------------------
try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(
        model_name="models/gemini-pro-latest",
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

# -----------------------------
# --- CHAT HISTORY INITIALIZATION ---
# -----------------------------
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
    st.session_state.history = []

# Display previous chat messages
for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["text"])

# -----------------------------
# --- STREAMLIT CHAT LOGIC ---
# -----------------------------
if user_input := st.chat_input("Ask your question..."):

    # Store and display user message
    st.session_state.history.append({"role": "user", "text": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get AI response
    try:
        prompt = f"Respond in your signature reflective, poetic tone.\nUser: {user_input}"
        response = st.session_state.chat.send_message(prompt, stream=False)
        ai_text = response.text

        # Store and display AI response
        st.session_state.history.append({"role": "assistant", "text": ai_text})
        with st.chat_message("assistant"):
            st.markdown(ai_text)

        # -----------------------------
        # --- BROWSER-COMPATIBLE TTS ---
        # -----------------------------
        try:
            # Use a temporary file to avoid conflicts
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                tts = gTTS(text=ai_text, lang="hi", slow=False)
                tts.save(tmp_file.name)
                tmp_file_path = tmp_file.name

            # Play audio in Streamlit
            with open(tmp_file_path, "rb") as f:
                st.audio(f.read(), format="audio/mp3")

            # Delete temporary file
            os.remove(tmp_file_path)

        except Exception as e:
            st.warning(f"Audio generation error: {e}")

    except Exception as e:
        st.error(f"Error generating AI response: {e}")
