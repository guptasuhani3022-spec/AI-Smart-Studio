import streamlit as st
import pandas as pd
import plotly.express as px

from modules.sentiment import analyze_sentiment
from modules.summarizer import generate_extractive_summary, summarize_with_api
from modules.generator import generate_short_content

# Page Config
st.set_page_config(
    page_title="AI Smart Studio | Ultra Neon Edition",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ULTRA LUXURY CYBERPUNK / NEON GLASSMORPHISM CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;700;800&display=swap');
    
    * {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Main Background with Deep Aurora Glow */
    .stApp {
        background: radial-gradient(circle at 15% 15%, #2a0845 0%, #12002b 40%, #080016 100%);
        color: #f1f5f9;
    }
    
    /* Glowing Top Banner */
    .hero-container {
        position: relative;
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 24px;
        padding: 32px;
        margin-bottom: 28px;
        box-shadow: 0 20px 50px rgba(123, 31, 162, 0.25), inset 0 0 20px rgba(255, 0, 128, 0.1);
        overflow: hidden;
    }
    
    .hero-container::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255, 0, 128, 0.15) 0%, transparent 60%);
        pointer-events: none;
    }
    
    .hero-title {
        font-size: 2.8rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        background: linear-gradient(135deg, #ff007f 0%, #7928ca 40%, #00dfd8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 6px;
        text-shadow: 0 0 30px rgba(255, 0, 128, 0.3);
    }
    
    .hero-badge {
        display: inline-block;
        padding: 6px 16px;
        border-radius: 50px;
        background: linear-gradient(90deg, rgba(255, 0, 128, 0.2), rgba(0, 223, 216, 0.2));
        border: 1px solid rgba(255, 0, 128, 0.4);
        color: #00dfd8;
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 12px;
    }
    
    .hero-subtitle {
        color: #cbd5e1;
        font-size: 1.1rem;
        font-weight: 400;
    }
    
    /* Cyberpunk Metric Cards */
    .metric-card-neon {
        background: rgba(20, 10, 38, 0.6);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 0, 128, 0.2);
        border-radius: 18px;
        padding: 20px 16px;
        text-align: center;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    }
    
    .metric-card-neon:hover {
        transform: translateY(-6px) scale(1.02);
        border-color: #00dfd8;
        box-shadow: 0 15px 35px rgba(0, 223, 216, 0.3);
    }
    
    .metric-val-neon {
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #00dfd8, #007cf0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .metric-lbl-neon {
        font-size: 0.78rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        font-weight: 700;
        margin-top: 4px;
    }
    
    /* Neon Glass Result Box */
    .neon-glass-box {
        background: rgba(15, 7, 32, 0.75);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(121, 40, 202, 0.4);
        border-left: 5px solid #ff007f;
        border-radius: 16px;
        padding: 24px;
        margin-top: 20px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.6), inset 0 0 15px rgba(121, 40, 202, 0.15);
        font-size: 1.05rem;
        line-height: 1.7;
    }
    
    /* Glowing Action Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #ff007f 0%, #7928ca 50%, #00dfd8 100%) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 14px !important;
        padding: 14px 28px !important;
        font-size: 1.05rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.5px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 8px 25px rgba(255, 0, 128, 0.4) !important;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px) scale(1.01) !important;
        box-shadow: 0 12px 35px rgba(0, 223, 216, 0.6) !important;
    }
    
    /* Custom Sidebar Aesthetics & Bright Text */
    section[data-testid="stSidebar"] {
        background-color: rgba(10, 4, 22, 0.95) !important;
        border-right: 1px solid rgba(255, 0, 128, 0.2) !important;
    }

    /* Make Sidebar Widget Labels & Titles Bright Cyan/White */
    div[data-testid="stWidgetLabel"] p, label p, .stMarkdown p {
        color: #ffffff !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
    }

    /* Transform Sidebar Radio Buttons into Glowing Neon Cards */
    div[data-testid="stRadio"] label {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 0, 128, 0.25) !important;
        border-radius: 14px !important;
        padding: 12px 18px !important;
        margin-bottom: 10px !important;
        transition: all 0.3s ease !important;
    }

    div[data-testid="stRadio"] label p {
        color: #e2e8f0 !important;
        font-size: 1.02rem !important;
        font-weight: 700 !important;
    }

    div[data-testid="stRadio"] label:hover {
        border-color: #00dfd8 !important;
        background: rgba(0, 223, 216, 0.12) !important;
        box-shadow: 0 0 15px rgba(0, 223, 216, 0.3) !important;
    }

    /* Style Radio Circle Indicator */
    div[data-testid="stRadio"] label[data-checked="true"] {
        background: linear-gradient(135deg, rgba(255, 0, 128, 0.35), rgba(121, 40, 202, 0.45)) !important;
        border: 1.5px solid #ff007f !important;
        box-shadow: 0 0 20px rgba(255, 0, 128, 0.5) !important;
    }

    div[data-testid="stRadio"] label[data-checked="true"] p {
        color: #ffffff !important;
        font-weight: 800 !important;
    }

    /* Style Text Areas, Inputs & Selectbox */
    .stTextArea textarea, .stTextInput input, .stSelectbox select {
        background: rgba(15, 7, 32, 0.8) !important;
        border: 1px solid rgba(255, 0, 128, 0.3) !important;
        border-radius: 14px !important;
        color: #ffffff !important;
        font-size: 1rem !important;
    }
    
    .stTextArea textarea:focus, .stTextInput input:focus {
        border-color: #00dfd8 !important;
        box-shadow: 0 0 20px rgba(0, 223, 216, 0.4) !important;
    }
    </style>
""", unsafe_allow_html=True)

# HERO HEADER
st.markdown("""
    <div class="hero-container">
        <div class="hero-badge">⚡ FUTURE AI STUDIO • NO API NEEDED</div>
        <div class="hero-title">AI Smart Studio</div>
        <div class="hero-subtitle">Next-Gen Intelligence Engine for Sentiment Analytics, Text Summarization & Content Creation</div>
    </div>
""", unsafe_allow_html=True)

# SIDEBAR NAVIGATION
with st.sidebar:
    st.markdown("<h2 style='background: linear-gradient(90deg, #ff007f, #00dfd8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>⚡ CONTROL PANEL</h2>", unsafe_allow_html=True)
    
    app_mode = st.radio(
        "Choose AI Module:",
        ["📊 Sentiment & Emotion Matrix", "📝 Smart Text Summarizer", "✨ Creative Content Studio"]
    )
    
    st.divider()
    
    st.markdown("<h4 style='color: #00dfd8;'>⚙️ Processing Engine</h4>", unsafe_allow_html=True)
    api_provider = st.selectbox("Engine Mode", ["Offline (Built-in Ultra NLP)", "Google Gemini API"])
    api_key = ""
    if api_provider == "Google Gemini API":
        api_key = st.text_input("Gemini API Key", type="password")
        
    st.divider()
    st.caption("✨ Designed with Futuristic Cyberpunk Aesthetics")

# 1. SENTIMENT & EMOTION MATRIX
if app_mode == "📊 Sentiment & Emotion Matrix":
    st.markdown("<h2 style='color: #ff007f;'>📊 Sentiment & Emotion Intelligence</h2>", unsafe_allow_html=True)
    st.write("Deep neural tone detection, polarity scoring, and emotional distribution analysis.")
    
    user_text = st.text_area(
        "Input Text for Analysis:",
        placeholder="Paste customer reviews, tweets, feedback, or any text here...",
        height=140
    )
    
    if st.button("🚀 ANALYZE SENTIMENT MATRIX", use_container_width=True):
        if not user_text.strip():
            st.warning("⚠️ Please provide text input for analysis!")
        else:
            with st.spinner("Processing NLP tensor matrix..."):
                res = analyze_sentiment(user_text)
                st.divider()
                
                c1, c2, c3, c4 = st.columns(4)
                with c1:
                    st.markdown(f'''
                        <div class="metric-card-neon">
                            <div class="metric-lbl-neon">EMOTIONAL TONE</div>
                            <div class="metric-val-neon">{res["emoji"]} {res["label"]}</div>
                        </div>
                    ''', unsafe_allow_html=True)
                with c2:
                    st.markdown(f'''
                        <div class="metric-card-neon">
                            <div class="metric-lbl-neon">COMPOUND SCORE</div>
                            <div class="metric-val-neon">{res["compound"]}</div>
                        </div>
                    ''', unsafe_allow_html=True)
                with c3:
                    st.markdown(f'''
                        <div class="metric-card-neon">
                            <div class="metric-lbl-neon">POLARITY INDEX</div>
                            <div class="metric-val-neon">{res["polarity"]}</div>
                        </div>
                    ''', unsafe_allow_html=True)
                with c4:
                    st.markdown(f'''
                        <div class="metric-card-neon">
                            <div class="metric-lbl-neon">SUBJECTIVITY</div>
                            <div class="metric-val-neon">{res["subjectivity"]}</div>
                        </div>
                    ''', unsafe_allow_html=True)
                
                st.write("")
                st.write("")
                
                col_chart, col_meta = st.columns([3, 2])
                with col_chart:
                    st.markdown("### 📈 Emotion Breakdown Matrix")
                    df = pd.DataFrame({
                        "Sentiment": ["Positive", "Neutral", "Negative"],
                        "Score (%)": [res["pos"], res["neu"], res["neg"]]
                    })
                    fig = px.bar(
                        df, 
                        x="Sentiment", 
                        y="Score (%)", 
                        color="Sentiment",
                        color_discrete_map={"Positive": "#00dfd8", "Neutral": "#a855f7", "Negative": "#ff007f"},
                        text_auto=True
                    )
                    fig.update_layout(
                        paper_bgcolor="rgba(0,0,0,0)",
                        plot_bgcolor="rgba(0,0,0,0)",
                        font=dict(color="#f1f5f9", family="Plus Jakarta Sans"),
                        showlegend=False,
                        height=320,
                        yaxis=dict(gridcolor="rgba(255,255,255,0.08)")
                    )
                    st.plotly_chart(fig, use_container_width=True)
                    
                with col_meta:
                    st.markdown("### 💡 Deep Insights")
                    st.markdown(f"""
                    <div class="neon-glass-box">
                        <b>Tone Status:</b> <span style="color:#00dfd8;">{res['label']} ({res['emoji']})</span><br><br>
                        • <b>Subjectivity Ratio:</b> <span style="color:#00dfd8; font-weight:bold;">{res['subjectivity']}</span> (Higher means opinion-based text)<br>
                        • <b>Total Words:</b> <span style="color:#00dfd8; font-weight:bold;">{len(user_text.split())}</span><br>
                        • <b>Character Length:</b> <span style="color:#00dfd8; font-weight:bold;">{len(user_text)}</span>
                    </div>
                    """, unsafe_allow_html=True)

# 2. SMART TEXT SUMMARIZER
elif app_mode == "📝 Smart Text Summarizer":
    st.markdown("<h2 style='color: #7928ca;'>📝 Ultra Text Summarizer Engine</h2>", unsafe_allow_html=True)
    st.write("Extract core ideas, key takeaways, and bullet summaries from long documents.")
    
    long_text = st.text_area("Paste Document or Essay Text:", height=180, placeholder="Paste long text here...")
    
    col_sl, col_inf = st.columns(2)
    with col_sl:
        summary_len = st.slider("Target Summary Sentences:", 1, 7, 3)
    with col_inf:
        engine_txt = "Google Gemini AI" if (api_provider == "Google Gemini API" and api_key) else "Offline Extractive NLP"
        st.markdown(f"**Current Engine:** <span style='color:#00dfd8; font-weight:bold;'>{engine_txt}</span>", unsafe_allow_html=True)
        
    if st.button("✨ GENERATE SUMMARY", use_container_width=True):
        if not long_text.strip():
            st.warning("⚠️ Please paste text to summarize!")
        else:
            with st.spinner("Extracting key insights..."):
                if api_provider == "Google Gemini API" and api_key:
                    res = summarize_with_api(long_text, api_key, provider="gemini")
                else:
                    res = generate_extractive_summary(long_text, max_sentences=summary_len)
                    
                st.markdown("### 📌 Executive Summary")
                st.markdown(f"""
                <div class="neon-glass-box">
                    {res['summary']}
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("### 🎯 Key Actionable Takeaways")
                for bp in res["bullet_points"]:
                    st.markdown(f"<div style='background: rgba(255,255,255,0.03); border-radius: 10px; padding: 10px 16px; margin-bottom: 8px; border-left: 3px solid #00dfd8;'>{bp}</div>", unsafe_allow_html=True)
                    
                st.caption(f"⏱️ Estimated Reading Time Saved: ~{res['reading_time_min']} mins")

# 3. CREATIVE CONTENT STUDIO
elif app_mode == "✨ Creative Content Studio":
    st.markdown("<h2 style='color: #00dfd8;'>✨ Creative AI Content Generator</h2>", unsafe_allow_html=True)
    st.write("Generate viral posts, headlines, emails, and story concepts with smart AI templates.")
    
    c_in1, c_in2 = st.columns([2, 1])
    with c_in1:
        topic_input = st.text_input("Enter Topic / Keyword:", placeholder="e.g. Artificial Intelligence, Python Projects, Startup Launch...")
    with c_in2:
        content_type = st.selectbox("Content Format:", ["LinkedIn Post", "Twitter/X Post", "Catchy Headline", "Professional Email", "Short Creative Story"])
        
    if st.button("🚀 GENERATE CREATIVE CONTENT", use_container_width=True):
        if not topic_input.strip():
            st.warning("⚠️ Please provide a topic!")
        else:
            with st.spinner("Crafting content..."):
                provider = "gemini" if api_provider == "Google Gemini API" else None
                generated_result = generate_short_content(topic_input, content_type, api_key=api_key if provider else None, provider=provider)
                
                st.markdown(f"### 🎉 Generated {content_type}")
                st.code(generated_result, language="text")
                st.success("💡 Tip: Click the copy icon in the top right corner of the box above to copy!")

# Footer
st.divider()
st.markdown("<div style='text-align: center; color: #64748b; font-size: 0.9rem;'>⚡ AI Smart Studio • Cyberpunk Glassmorphism Edition</div>", unsafe_allow_html=True)
