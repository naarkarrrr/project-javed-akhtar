# Project: Javed Akhtar AI Chatbot

An AI-driven chatbot emulating the persona of Javed Akhtar — the legendary poet, lyricist, and thinker. Built using Google Generative AI and Streamlit, this project offers a conversational experience that blends English, Hindi, and Urdu with poetic rhythm and wit.

> ⚠️ **Work in Progress:** This project is still under development. Features, responses, and TTS functionality are being improved continuously.

---

## Features

* **Conversational AI**: Engage in dialogues with an AI modeled after Javed Akhtar.
* **Multilingual Support**: Responses in English, Hindi, and Urdu.
* **Text-to-Speech**: Listen to AI responses with integrated audio playback.
* **Streamlit Interface**: User-friendly web interface for seamless interaction.
* **In Development**: Additional features, voice cloning, and optimizations are planned.

---

## Planned Features

* **Voice Cloning**: Integrate Javed Akhtar’s real voice for more authentic audio responses.
* **Enhanced TTS**: Improve text-to-speech for natural emotion and rhythm.
* **Expanded Persona**: Add more depth to AI’s knowledge of poetry, philosophy, and quotes.
* **Frontend Improvements**: Better chat UI, responsive design, and user-friendly features.
* **Deployment Optimization**: Faster load times and smoother audio streaming.

---

## Project Structure

```
project-javed-akhtar/
├── .streamlit/
│   └── secrets.toml          # Store your API keys securely
├── netlify-chatbot/          # Optional: Frontend deployment folder
├── node_modules/             # Node.js dependencies (if applicable)
├── package-lock.json         # Lock file for Node.js dependencies
├── package.json              # Node.js project configuration
├── requirements.txt          # Python dependencies
├── response.mp3              # Sample audio response
├── test.py                   # Test script for local development
└── chatbot_v4_webapp.py      # Main Streamlit app for chatbot interaction
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/naarkarrrr/project-javed-akhtar.git
cd project-javed-akhtar
```

### 2. Set Up Python Environment

```bash
python -m venv bark_env
.\bark_env\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure Google AI API Key

* Create a file named `secrets.toml` inside the `.streamlit/` directory.
* Add your API key as follows:

```toml
[google_ai]
api_key = "YOUR_GOOGLE_AI_API_KEY"
```

---

### 4. Run the Application

```bash
streamlit run chatbot_v4_webapp.py
```

---

## Deployment

### Streamlit Cloud

1. Push your repository to GitHub.
2. Visit [Streamlit Cloud](https://share.streamlit.io/).
3. Connect your GitHub repository.
4. Deploy the app and access it via the provided URL.

### Netlify (Optional)

For deploying the frontend separately:

1. Ensure your `netlify-chatbot/` directory contains the necessary frontend files.
2. Create a `netlify.toml` configuration file.
3. Deploy using Netlify's platform.

---

## Dependencies

* **Python**: 3.x
* **Streamlit**: For building the web interface.
* **google-generativeai**: To interact with Google's Generative AI.
* **gtts**: For text-to-speech functionality.

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

If you want, I can also **draft a shorter, GitHub-friendly “landing section”** with badges and a demo GIF for your repo so it **looks super professional on GitHub**.

Do you want me to do that next?
