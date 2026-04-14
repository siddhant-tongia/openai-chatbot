# OpenAI Chatbot

A simple conversational chatbot that takes text input and returns 
text responses using an LLM via the OpenRouter API. It remembers 
previous messages in the conversation, so it can give context-aware 
answers.

## What I learned
- How to use environment variables with `.env`
- What an API is and how API keys work
- How to integrate the OpenAI library
- How conversation memory is implemented in a chatbot

## How to run

1. Clone or copy the code into a file
2. Install dependencies:
   pip install openai python-dotenv
3. Create a `.env` file and add your API key:
   OPENAI_API_KEY=your_key_here
4. Run in terminal:
   python my_chat.py
5. Type your question and press Enter
6. Type `quit` to exit

## Tech used
- Python
- OpenAI library
- OpenRouter API
- python-dotenv
- os
