# Daily Motivation Generator

## Overview
This is a Streamlit-based web application that generates personalized motivational quotes using AI. The app uses the Groq API (LLaMA3-70B model) to create motivational content based on the user's current mood or situation.

## Project Information
- **Framework**: Streamlit (Python)
- **AI Provider**: Groq API (LLaMA3-70B model)
- **Port**: 5000
- **Deployment**: Autoscale deployment configuration

## Recent Changes
- **2025-10-22**: Project imported from GitHub and configured for Replit environment
  - Installed Python 3.11 and all dependencies
  - Configured Streamlit to work with Replit's proxy (allows all hosts)
  - Set up workflow to run on port 5000
  - Configured deployment for autoscale
  - Added comprehensive .gitignore for Python projects
  - Set up GROQ_API_KEY as environment secret

## Architecture
- **app.py**: Main application file containing Streamlit UI and Groq API integration
- **.streamlit/config.toml**: Streamlit configuration (enables proxy support)
- **requirements.txt**: Python dependencies

## Environment Variables
- **GROQ_API_KEY**: API key for Groq service (stored in Replit Secrets)

## Features
- Mood selection from 7 different emotional states
- AI-generated personalized motivational quotes
- Simple, clean user interface
- Error handling for API failures
