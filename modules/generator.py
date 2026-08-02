import random
import requests

TEMPLATES = {
    "LinkedIn Post": [
        """🚀 **THE ULTIMATE DEEP DIVE: Why {topic} is Transforming the Tech Landscape in 2026**

Artificial Intelligence and modern software architecture are evolving faster than ever. If you're a developer, founder, or tech enthusiast, understanding **{topic}** is no longer optional—it's a critical game-changer.

Over the past few months of building and testing, I've realized that {topic} solves three massive pain points:

1️⃣ **Eliminating Manual Overhead**: Instead of spending hours writing repetitive boilerplate logic, modern frameworks handle heavy lifting automatically.
2️⃣ **Privacy & Local Independence**: You don't always need expensive cloud APIs. Running lightweight, zero-cost Python algorithms locally gives you 100% control over your data.
3️⃣ **Seamless User Experience**: Combining powerful backend processing with sleek, intuitive UI (like Streamlit glassmorphism) turns complex tech into an effortless user experience.

💡 **Key Takeaway for Tech Professionals:**
Focusing on core user value always wins over over-engineering. Whether you're building open-source projects or enterprise solutions, keeping your architecture modular, fast, and accessible will set you apart.

What are your thoughts on {topic}? Have you implemented similar solutions in your projects? Let's start a conversation in the comments below! 👇

#{clean_topic} #SoftwareEngineering #Python #AI #TechInnovation #CodingCommunity #OpenSource #Productivity""",

        """🔥 **Case Study: How Building a Project Around {topic} Changed My Approach to Development**

When I first started exploring **{topic}**, I realized most existing tutorials overcomplicate the setup. They force developers into expensive API subscriptions or massive multi-layer frameworks when a clean, elegant Python solution is all you really need.

Here is the exact step-by-step framework I followed:

📌 **Step 1: Focus on the Core Problem**
Before writing a single line of code, identify what outcome the user wants from {topic}.

📌 **Step 2: Leverage Built-in NLP & Smart Algorithms**
By using local NLP engines, we achieve instant response times, zero latency, and zero running costs.

📌 **Step 3: Craft a Stunning, Futuristic Interface**
A great engine needs a great UI! Using modern glassmorphic designs, vibrant color schemes, and interactive data visualization (like Plotly charts) makes the app feel like a premium product.

🌟 **The Result:** An application that runs 100% offline, costs $0 to host locally, and delivers high-value AI analytics in seconds!

If you're building in public or learning Python, don't be afraid to experiment with {topic}. 

Drop a "🚀" in the comments if you'd like to see more projects like this!

#{clean_topic} #PythonProjects #Streamlit #BuildInPublic #Developers #MachineLearning #WebDev #Innovation""",

        """💡 **Mastering {topic}: 5 Essential Insights Every Tech Professional Should Know**

As technology continues to reshape how we create, analyze, and build products, **{topic}** has emerged as a key area of focus for modern innovators.

Here is a breakdown of what makes {topic} so powerful:

🔹 **1. High Efficiency & Automation**: Automates tedious manual tasks so you can focus on creative problem-solving.
🔹 **2. Cost Effectiveness**: Solves real-world problems using free, open-source libraries without mandatory paid API subscriptions.
🔹 **3. Data Privacy First**: Processing information locally ensures sensitive data never leaves your environment.
🔹 **4. Scalable & Modular Architecture**: Easy to upgrade, customize, and integrate into existing tech stacks.
🔹 **5. High Visual Impact**: Pairs seamlessly with modern dashboards and interactive charts for immediate stakeholder buy-in.

🎯 **Final Thought:**
The future belongs to creators who build fast, iterate relentlessly, and focus on delivering genuine value with tools like {topic}.

What's your favorite aspect of {topic}? Share your thoughts and let's connect! 💬

#{clean_topic} #Technology #ArtificialIntelligence #SoftwareDevelopment #CareerInTech #LearningToCode #DataScience"""
    ],
    "Twitter/X Post": [
        "🔥 Quick breakdown on {topic}:\n\n- Game changer for creators & devs\n- Saves 10+ hours of manual work\n- Runs 100% offline & free\n\nAre you leveraging {topic} yet? 💭 #{clean_topic} #Tech",
        "⚡ 3 simple steps to master {topic}:\n\n1. Start with clean, modular logic\n2. Design an intuitive UI\n3. Iterate fast based on feedback\n\nBookmark this thread for later! 📌 #{clean_topic} #BuildInPublic",
        "🧠 Most people overcomplicate {topic}.\n\nReality: You can achieve 90% of the value using clean Python algorithms without paying for API keys.\n\nSimplicity always wins. 🚀 #{clean_topic} #AI #Python"
    ],
    "Catchy Headline": [
        "🔥 Unlocking the True Power of {topic}: Everything You Need to Know",
        "🚀 Why {topic} is the Next Big Breakthrough in 2026",
        "💡 10 Game-Changing Ways {topic} Will Transform Your Workflow",
        "⚡ Stop Overcomplicating {topic}! Here's the Simple Python Solution"
    ],
    "Professional Email": [
        "Subject: Proposal & Key Discussion regarding {topic}\n\nHi Team,\n\nI hope this email finds you well.\n\nI wanted to share a quick proposal regarding our implementation of {topic}. By leveraging streamlined processing, we can significantly reduce manual overhead while boosting output quality.\n\nKey Highlights:\n- Faster delivery cycles\n- Reduced dependency on external services\n- High customizability for client needs\n\nPlease let me know your availability this week for a brief 15-minute discussion.\n\nBest regards,\n[Your Name]",

        "Subject: Project Update: Breakthroughs in {topic}\n\nHello [Name],\n\nFollowing up on our recent project goals, I am pleased to share that our work on {topic} is progressing ahead of schedule.\n\nWe have successfully implemented key features that ensure high reliability and zero downtime.\n\nLooking forward to your feedback on the demo.\n\nBest regards,\n[Your Name]"
    ],
    "Short Creative Story": [
        "In a world driven by endless data streams, {topic} became the spark of a new technological renaissance. Developers across the globe discovered that when they combined human creativity with {topic}, complex challenges transformed into effortless solutions. The journey into the future had officially begun...",

        "Late one night in the lab, a developer pushed a small piece of code for {topic}. What started as a simple experiment suddenly unlocked unprecedented speed and clarity. Within hours, the application was serving users worldwide, proving that great ideas need only a spark to change everything."
    ]
}

def generate_short_content(topic: str, content_type: str, api_key: str = None, provider: str = None) -> str:
    """
    Generates high-quality, rich, detailed content based on topic and content type.
    """
    if api_key and provider == "gemini":
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
        prompt = f"Write a viral, detailed, multi-paragraph LinkedIn post about topic: '{topic}'. Use great formatting, emojis, bullet points, step-by-step points, and actionable takeaways."
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        try:
            res = requests.post(url, json=payload, timeout=10)
            if res.status_code == 200:
                data = res.json()
                return data['candidates'][0]['content']['parts'][0]['text']
        except Exception:
            pass
            
    clean_topic = "".join(e for e in topic if e.isalnum())
    template_list = TEMPLATES.get(content_type, TEMPLATES["Catchy Headline"])
    selected_template = random.choice(template_list)
    return selected_template.format(topic=topic, clean_topic=clean_topic)
