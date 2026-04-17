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
* What is Twilio Account SID and Twilio Auth TOKEN
* How to convert Python data to JSON and then to bytes for file download

## How to run

1. Clone the repository
2. Install dependencies:
   pip install openai python-dotenv flask twilio
3. Create a `.env` file and add your credentials:
   API_KEY=your_openrouter_key_here
   TWILIO_ACCOUNT_SID=your_sid_here
   TWILIO_AUTH_TOKEN=your_token_here
   TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
4. Run in terminal:
   python app.py
5. Test API routes using Thunder Client or Postman
6. For WhatsApp — connect Twilio sandbox and set webhook URL to:
   http://localhost:5000/whatsapp (local)
   or your Railway URL (production)
7. To receive messages — someone must message your Twilio number first
8. To send messages proactively — use the /send-whatsapp route

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

### 6. `/analytics/<user_id>`

* Method: GET
* Description: Give all the message information for paricular user

### 7. `/analytics`

* Method: GET
* Description: Give all the message information for all user

### 8. `/export/<user_id>`

* Method: GET
* Description: Give access to dowload the chat.

### 9. `/whatsapp_send`

* Method: POST
* Description: Bot can send the message on whatsapp.

## Tech used

* Python
* OpenAI library
* OpenRouter API
* python-dotenv
* os
* Flask
* Railway
* Twilio
