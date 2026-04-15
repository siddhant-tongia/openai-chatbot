# OpenAI Chatbot API

A Flask-based conversational API that takes text input and returns
responses using an LLM via the OpenRouter API. It supports multiple users
and maintains conversation memory per user, allowing context-aware
interactions.

## What I learned

* How to use environment variables with `.env`
* What an API is and how API keys work
* How to integrate the OpenAI library
* How conversation memory is implemented in a chatbot
* How to save data in a JSON file
* How to build APIs using Flask
* Understanding REST APIs
* Difference between GET and POST requests
* How decorators work in Flask

## How to run

1. Clone or copy the code into a file
2. Install dependencies:
   pip install openai python-dotenv flask
3. Create a `.env` file and add your API key:
   API_KEY=your_key_here
4. Run in terminal:
   python app.py
5. Use API endpoints via tools like Postman or browser

## Routes

### 1. `/chat`

* Method: POST
* Description: Sends user message and receives chatbot response

### 2. `/history/<user_id>`

* Method: GET
* Description: Returns conversation history for a user

### 3. `/clear/<user_id>`

* Method: GET
* Description: Returns the status of chat


## Tech used

* Python
* Flask
* OpenAI library
* OpenRouter API
* python-dotenv
* os
