# OpenAI Whatsapp Chatbot

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
* What is railway and how to deploy the website
* How to work on Twilio website and what is TwiML

## How to run

1. Clone the repository
2. Install dependencies:
   pip install openai python-dotenv flask twilio
3. Create a `.env` file and add your API key:
   API_KEY=your_openrouter_key_here
4. Run in terminal:
   python app.py
5. Test API routes using Thunder Client or Postman
6. For WhatsApp — connect Twilio sandbox and set webhook URL to:
   http://localhost:5000/whatsapp (local) or your Railway URL (production)

## Routes

### 1. `/`
* This is Home Route

### 2. `/chat`

* Method: POST
* Description: Sends user message and receives chatbot response

### 3. `/whatsapp`
* Method: POST
* Description: Sends user message through whatsapp and give response to whatsapp itself with few seconds

### 4. `/history/<user_id>`

* Method: GET
* Description: Returns conversation history for a user

### 5. `/clear/<user_id>`

* Method: POST
* Description: It clear the conversation history 


## Tech used

* Python
* Flask
* Railway
* Twilio
* OpenAI library
* OpenRouter API
* python-dotenv
* os
