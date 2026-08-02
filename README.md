# ⚡ AI Smart Studio (Python + Streamlit)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Plotly-Data_Viz-3F51B5?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly">
  <img src="https://img.shields.io/badge/NLP-VADER%20%26%20TextBlob-green?style=for-the-badge" alt="NLP">
  <img src="https://img.shields.io/badge/UI-Cyberpunk_Glassmorphism-purple?style=for-the-badge" alt="Glassmorphism">
</p>

> **AI Smart Studio** is a futuristic, ultra-fast web application built with **Python** and **Streamlit**. It offers offline Natural Language Processing (NLP) tools for sentiment analytics, text summarization, and long-form creative content generation—all inside a stunning **Cyberpunk Glassmorphism UI**.

---

## 🌟 Key Features

### 1. 📊 Sentiment & Emotion Matrix
- **Tone Detection**: Classifies text as **Positive 😃**, **Negative 😔**, or **Neutral 😐**.
- **Deep Metrics**: Calculates **Compound Score**, **Polarity Index**, and **Subjectivity Ratio** (Opinion vs Fact).
- **Interactive Visualizations**: Dynamic bar chart matrix powered by **Plotly**.

### 2. 📝 Smart Text Summarizer
- **Extractive NLP**: Frequency-scoring algorithm that extracts core themes from articles & documents.
- **Actionable Takeaways**: Converts long paragraphs into key bullet points.
- **Reading Time Metric**: Shows estimated reading time saved.

### 3. ✨ Creative Content Studio
- **Long-Form Viral LinkedIn Posts**: Generates multi-paragraph, storytelling LinkedIn posts complete with step-by-step insights, emojis, and hashtags.
- **Twitter/X Threads**: Punchy, high-engagement tweets.
- **Catchy Headlines & Professional Emails**: Instant templates for blogs and business communications.

### 4. ⚙️ Dual Processing Engine
- ⚡ **Offline Engine (100% Free)**: Powered by local VADER & TextBlob NLP algorithms. No API key required!
- 🔑 **Google Gemini API Engine (Optional)**: Seamless integration for advanced LLM abstractive capabilities.

---

## 🎨 UI Aesthetic Highlights

- **Aurora Space Background**: Deep dark purple gradient theme (`#12002b`).
- **Cyberpunk Glassmorphism**: Translucent cards with `backdrop-filter: blur(20px)`.
- **Interactive Neon Lighting**: Glowing buttons, cyan accents, and hover micro-animations.
- **Glowing Sidebar Navigation**: Bright custom radio cards designed for high readability.

---

## 🛠️ Tech Stack

- **Language**: Python 3.10+
- **Frontend Framework**: Streamlit
- **Data Visualization**: Plotly Express & Pandas
- **NLP Engines**: VADER Sentiment (`vaderSentiment`), TextBlob (`textblob`)
- **HTTP/API**: Requests

---

## 🚀 Quick Setup & Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/ai-smart-studio.git
cd ai-smart-studio
```

### Step 2: Install Dependencies
Run the following command in your terminal:
```bash
python -m pip install -r requirements.txt
```

### Step 3: Launch the App
```bash
python -m streamlit run app.py
```

Open your browser at `http://localhost:8501` to use **AI Smart Studio**!

---

## 📁 Project Structure

```
ai_streamlit_app/
│
├── app.py                # Main Streamlit Application & Cyberpunk UI Layout
├── requirements.txt      # Python Dependencies
├── README.md             # GitHub Project Documentation
└── modules/
    ├── __init__.py
    ├── sentiment.py      # VADER & TextBlob Sentiment Logic
    ├── summarizer.py     # Frequency-based Extractive Summarizer
    └── generator.py      # Rich Viral Content Templates Engine
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/your-username/ai-smart-studio/issues).

---

## 📜 License

This project is [MIT](LICENSE) licensed. Feel free to use, modify, and distribute!
