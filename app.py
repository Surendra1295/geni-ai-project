import streamlit as st
import requests
import os
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
def generate_motivation(mood):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "user", "content": f"Give me a motivational quote for someone who is {mood.lower()}."}
        ],
        "temperature": 0.7
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

# Streamlit UI
st.set_page_config(page_title="Daily Motivation Generator")
st.title("🌟 Daily Motivation Generator")
st.write("Select your current mood or situation, and receive a motivational quote.")

mood = st.selectbox("Choose your mood/situation:", [
    "Feeling anxious",
    "Need focus",
    "Lack of confidence",
    "Feeling low",
    "Stressed out",
    "Unmotivated",
    "Need positivity"
])

if st.button("💬 Generate Motivation"):
    try:
        with st.spinner("Generating..."):
            quote = generate_motivation(mood)
            st.success("Here's your quote:")
            st.text_area("💡 Motivational Quote", quote, height=150)
    except Exception as e:
        st.error(f"Failed to generate quote:\n{e}")
