import re
from collections import Counter
import requests

def generate_extractive_summary(text: str, max_sentences: int = 3) -> dict:
    """
    Extracts key sentences based on word frequency scoring (Offline Fast Summarizer).
    """
    cleaned = re.sub(r'[^\w\s]', '', text.lower())
    words = [word for word in cleaned.split() if len(word) > 3]
    
    if not words:
        return {"summary": text, "bullet_points": [text], "reading_time_min": 1}
    
    word_freq = Counter(words)
    
    # Split text into sentences
    sentences = re.split(r'(?<=[.!?]) +', text.strip())
    if len(sentences) <= max_sentences:
        bullet_points = [f"• {s.strip()}" for s in sentences if s.strip()]
        return {
            "summary": text.strip(),
            "bullet_points": bullet_points,
            "reading_time_min": max(1, round(len(words) / 200, 1))
        }
    
    # Score sentences
    sentence_scores = {}
    for i, sentence in enumerate(sentences):
        score = 0
        s_words = [w.lower() for w in re.findall(r'\w+', sentence) if len(w) > 3]
        for w in s_words:
            score += word_freq.get(w, 0)
        # Normalize by sentence length
        sentence_scores[i] = score / (len(s_words) + 1)
        
    # Select top sentences
    top_sentence_indices = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:max_sentences]
    top_sentence_indices.sort()
    
    summary_sentences = [sentences[i].strip() for i in top_sentence_indices]
    summary_text = " ".join(summary_sentences)
    bullet_points = [f"• {s}" for s in summary_sentences]
    
    return {
        "summary": summary_text,
        "bullet_points": bullet_points,
        "reading_time_min": max(1, round(len(words) / 200, 1))
    }

def summarize_with_api(text: str, api_key: str, provider: str = "gemini") -> dict:
    """
    Optional LLM API summarizer for advanced abstractive summaries.
    """
    if provider.lower() == "gemini":
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
        prompt = f"Summarize the following text in concise bullet points and a brief paragraph:\n\n{text}"
        payload = {
            "contents": [{"parts": [{"text": prompt}]}]
        }
        try:
            res = requests.post(url, json=payload, timeout=10)
            if res.status_code == 200:
                data = res.json()
                output_text = data['candidates'][0]['content']['parts'][0]['text']
                return {
                    "summary": output_text,
                    "bullet_points": [output_text],
                    "reading_time_min": max(1, round(len(text.split()) / 200, 1))
                }
        except Exception as e:
            pass
            
    # Fallback to local extractive summary if API fails or key not provided
    return generate_extractive_summary(text)
