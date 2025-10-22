# 🌟 Daily Motivation Generator using Generative AI (Groq)

This project is a simple web-based application that generates personalized motivational quotes based on a user's selected mood or situation. It leverages the power of **LLaMA 3.3 70B Versatile** from **Groq API** and is built with a clean, responsive interface using **Streamlit**.

---

## 🔍 Project Objective

To help users overcome emotional blocks like anxiety, stress, or lack of focus by providing **timely and personalized motivational quotes**, powered by **Generative AI**.

---

## 🚀 Features

- 🎯 Select from predefined moods/situations  
- 💡 Get AI-generated motivational quotes instantly  
- 🧠 Uses LLaMA 3.3 70B Versatile model via Groq API  
- 🖥️ Streamlit-based user interface (minimal and fast)

---

## 🛠️ Technologies Used

- Python  
- Streamlit  
- Groq API (LLaMA 3.3 70B Versatile model)  
- Requests  
- python-dotenv

---

## 📸 Demo

🌐 [Try it Live on Streamlit](https://surendra1295-geni-ai-project-app-tqygdg.streamlit.app/)  
📁 [View the GitHub Repository](https://github.com/Surendra1295/geni-ai-project.git)

---

## 📦 Setup Instructions

### 1. Clone this repository

```bash
git clone https://github.com/Surendra1295/geni-ai-project.git
cd geni-ai-project
```

### 2. Get Your Groq API Key

1. Visit [Groq Console](https://console.groq.com/)
2. Create a free account
3. Navigate to API Keys section
4. Generate a new API key

### 3. Configure Environment Variables

**For Local Development:**
```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your API key
GROQ_API_KEY=your_groq_api_key_here
```

**For Replit:**
- Use Replit Secrets (more secure)
- Add `GROQ_API_KEY` in the Secrets tab
- Replit Secrets take priority over .env files

**For Streamlit Cloud:**
- In deployment settings, go to "Advanced settings"
- Add `GROQ_API_KEY` in the Secrets section
- Format: `GROQ_API_KEY = "your_key_here"`

**Note:** The .env file is gitignored for security. Never commit API keys to version control!

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
streamlit run app.py
