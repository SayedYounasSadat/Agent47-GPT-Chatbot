# Agent47-GPT-Chatbot
A charismatic, Agent47-style AI chatbot that helps with programming and technology-related questions. Powered by OpenAI’s GPT-OSS-120B model via Hugging Face. The chatbot is designed to respond concisely, seriously, and with a cool personality.

Features

Conversational AI with a “hitman Agent47” personality.

Assists with programming, technology, and coding-related queries.

Simple, clean command-line interface.

Easy setup using a Hugging Face API token.

Supports multi-question sessions with graceful exit.

Requirements

Python 3.8+

openai Python package

Hugging Face API token (HF_TOKEN)

Installation

Clone the repository:

git clone https://github.com/your-username/agent47-gpt-chatbot.git
cd agent47-gpt-chatbot


Create and activate a virtual environment (recommended):

python3 -m venv venv
source venv/bin/activate


Install dependencies:

pip install openai


Set your Hugging Face token:

export HF_TOKEN="your_hugging_face_api_token_here"


Or you can insert the token directly in the script (not recommended for public repos).

Usage

Run the chatbot script:

python3 main.py


Type your programming or technology question and hit Enter.

Type exit or quit to end the session.

Example session:

Welcome! Ask anything (type 'exit' to quit).

Your question: How do I reverse a list in Python?
AI: You can use list[::-1] to reverse a list in Python quickly.

Your question: exit
Goodbye!
