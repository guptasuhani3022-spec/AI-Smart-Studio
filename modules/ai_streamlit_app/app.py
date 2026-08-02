import streamlit as st
import pandas as pd
import plotly.express as px

from modules.sentiment import analyze_sentiment
from modules.summarizer import generate_extractive_summary, summarize_with_api
from modules.generator import generate_short_content

st.set_page_config(
    page_title="AI Smart Studio | Python Streamlit AI App",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Glassmorphism Dark Theme Styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%);
        color: #f8fafc;
    }
    .header-card {
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 24px;
    }
    .header-title {
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(90deg, #38bdf8, #818cf8, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .metric-card {
        background: rgba(30, 41, 59, 0.5);
        border-radius: 12px;
        padding: 16px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        text-align: center;
    }
    .metric-value {
        font-size: 1.8rem;
        font-weight: 700;
        color: #38bdf8;
    }
    .metric-label {
        font-size: 0.85rem;
        color: #94a3b8;
        text-transform: uppercase;
    }
    .stButton>button {
        background: linear-gradient(90deg, #6366f1, #8b5cf6) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 10px 24px !important;
        font-weight: 600 !important;
    }
    .result-box {
        background: rgba(15, 23, 42, 0.6);
        border-radius: 12px;
        padding: 20px;
        border-left: 4px solid #818cf8;
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="header-card">
        <div class="header-title">🤖 AI Smart Studio</div>
        <div style="color: #94a3b8;">Multi-functional Python AI Suite for Text Analysis, Summarization & Short Content Generation</div>
    </div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("⚡ AI Controls")
    app_mode = st.radio(
        "Select Feature:",
        ["📊 Sentiment & Emotion Analyzer", "📝 Text Summarizer", "✨ Creative AI Content Writer"]
    )
    st.divider()
    st.subheader("⚙️ API Configuration (Optional)")
    api_provider = st.selectbox("API Provider", ["Offline (Built-in NLP)", "Google Gemini API"])
    api_key = ""
    if api_provider == "Google Gemini API":
        api_key = st.text_input("Gemini API Key", type="password")

if app_mode == "📊 Sentiment & Emotion Analyzer":
    st.subheader("📊 Text Sentiment & Emotion Analyzer")
    user_text = st.text_area("Enter text to analyze:", placeholder="Type or paste your content here...", height=150)
    
    if st.button("🚀 Analyze Sentiment", use_container_width=True):
        if not user_text.strip():
            st.warning("⚠️ Please enter some text to analyze!")
        else:
            res = analyze_sentiment(user_text)
            st.divider()
            
            c1, c2, c3, c4 = st.columns(4)
            with c1:
                st.markdown(f'<div class="metric-card"><div class="metric-label">Tone</div><div class="metric-value">{res["emoji"]} {res["label"]}</div></div>', unsafe_allow_html=True)
            with c2:
                st.markdown(f'<div class="metric-card"><div class="metric-label">Score</div><div class="metric-value">{res["compound"]}</div></div>', unsafe_allow_html=True)
            with c3:
                st.markdown(f'<div class="metric-card"><div class="metric-label">Polarity</div><div class="metric-value">{res["polarity"]}</div></div>', unsafe_allow_html=True)
            with c4:
                st.markdown(f'<div class="metric-card"><div class="metric-label">Subjectivity</div><div class="metric-value">{res["subjectivity"]}</div></div>', unsafe_allow_html=True)
                
            df = pd.DataFrame({
                "Sentiment": ["Positive", "Neutral", "Negative"],
                "Percentage": [res["pos"], res["neu"], res["neg"]]
            })
            fig = px.bar(df, x="Sentiment", y="Percentage", color="Sentiment", color_discrete_map={"Positive": "#22c55e", "Neutral": "#94a3b8", "Negative": "#ef4444"}, text_auto=True)
            fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font=dict(color="#f8fafc"))
            st.plotly_chart(fig, use_container_width=True)

elif app_mode == "📝 Text Summarizer":
    st.subheader("📝 Smart Text Summarizer")
    long_text = st.text_area("Paste text to summarize:", height=200)
    summary_len = st.slider("Target Sentences:", 1, 7, 3)
    
    if st.button("✨ Summarize Text", use_container_width=True):
        if not long_text.strip():
            st.warning("⚠️ Please enter text!")
        else:
            if api_provider == "Google Gemini API" and api_key:
                res = summarize_with_api(long_text, api_key, provider="gemini")
            else:
                res = generate_extractive_summary(long_text, max_sentences=summary_len)
            
            st.markdown(f'<div class="result-box">{res["summary"]}</div>', unsafe_allow_html=True)
            st.subheader("🎯 Key Points")
            for bp in res["bullet_points"]:
                st.write(bp)

elif app_mode == "✨ Creative AI Content Writer":
    st.subheader("✨ Creative AI Content Writer")
    topic_input = st.text_input("Topic:")
    content_type = st.selectbox("Format:", ["LinkedIn Post", "Twitter/X Post", "Catchy Headline", "Professional Email", "Short Creative Story"])
    
    if st.button("🚀 Generate Content", use_container_width=True):
        if not topic_input.strip():
            st.warning("⚠️ Enter a topic!")
        else:
            provider = "gemini" if api_provider == "Google Gemini API" else None
            generated_result = generate_short_content(topic_input, content_type, api_key=api_key if provider else None, provider=provider)
            st.code(generated_result, language="text")