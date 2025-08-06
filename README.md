---
title: Chatbot Rivan
emoji: 🐠
colorFrom: gray
colorTo: pink
sdk: gradio
sdk_version: 5.41.0
app_file: app.py
pinned: false
short_description: AI chatbot for professional & personal use
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

# 🤖 Rivan Custom Chatbot

Welcome to the **Rivan Custom Chatbot** — an AI-powered assistant built with OpenAI’s GPT-3.5 Turbo and Gradio.

---

## Features

- Interactive live chat interface
- Context-aware conversation powered by OpenAI API
- Clean and user-friendly UI with custom styling
- Reset conversation button to start fresh anytime

---

## How to Use

1. Type your message in the **Your Message** box.
2. Click **Send** to get a response from the assistant.
3. View the ongoing chat history below.
4. Click **Reset Conversation** to clear the chat and start anew.

---

## Deployment

This app is hosted for free on [Hugging Face Spaces](https://huggingface.co/spaces/Rivan17/chatbot-Rivan).

---

## Technical Details

- Built with [Gradio](https://gradio.app/)
- Powered by [OpenAI GPT-3.5 Turbo](https://platform.openai.com/docs/models/gpt-3-5)
- Uses environment variable `OPENAI_API_KEY` for API access

---

## Setup (for developers)

If you want to run or modify this chatbot locally:

1. Clone the repo
2. Create a Python virtual environment
3. Install dependencies:
   ```bash
   pip install -r requirements.txt

## Set your OpenAI API key as an environment variable:

export OPENAI_API_KEY="your_api_key_here" # Linux/macOS
setx OPENAI_API_KEY "your_api_key_here"   # Windows (PowerShell)

## Run the app

python app.py

## License
MIT License © 2025 Rivan

## Feedback & Contributions
Feel free to open issues or submit pull requests for improvements!

Thank you for using the Rivan Custom Chatbot!
