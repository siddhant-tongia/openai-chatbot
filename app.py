from dotenv import load_dotenv
from openai import OpenAI
from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
import os

load_dotenv()

# create flask app
app = Flask(__name__)

# create openai client using env variable
client = OpenAI(
    api_key = os.getenv("API_KEY"),
    base_url = "https://openrouter.ai/api/v1"
)
# empty conversations dictionary
conversations = {}

# Define system prompts for different business types
SYSTEM_PROMPTS = {
    "coaching": """You are a helpful customer support bot for an online coaching center.
Your job is to:
1. Answer questions about courses and pricing
2. Help students register for courses
3. Provide study tips and encouragement
4. Be friendly and motivating
Keep responses short and suitable for WhatsApp.""",
    
    "ecommerce": """You are a helpful customer support bot for an online store.
Your job is to:
1. Answer questions about products
2. Help customers find what they need
3. Process simple orders
4. Be friendly and helpful
Keep responses short and suitable for WhatsApp.""",
    
    "clinic": """You are a helpful appointment booking bot for a clinic.
Your job is to:
1. Help patients book appointments
2. Answer questions about services
3. Provide health tips
4. Be professional and caring
Keep responses short and suitable for WhatsApp.""",
    
    "restaurant": """You are a helpful order-taking bot for a restaurant.
Your job is to:
1. Help customers place orders
2. Answer questions about menu items
3. Provide delivery information
4. Be friendly and helpful
Keep responses short and suitable for WhatsApp."""
}

@app.route("/")
def home():
    return "Chatbot API is running "

# /chat route that accepts POST
@app.route("/chat",methods=['POST'])
def user_info():
    # get user_id and message from request
    data = request.json
    user_id = data.get('user_id')
    user_input = data.get('message')
    business_type = data.get('business_type', 'coaching')

    if not user_id or not user_input:
        return jsonify({"error": "Missing user_id or message"}), 400

    # if user is new, create dict with messages and business_type
    if user_id not in conversations:
        conversations[user_id] = {
            "messages": [],
            "business_type": business_type
        }

    # append user message to their list
    conversations[user_id]["messages"].append({"role": "user", "content": user_input})

    # Look up the business instructions
    system_prompt = SYSTEM_PROMPTS.get(business_type, "You are a helpful assistant")

    # call openai api with their message history
    try:
        full_messages = [{"role": "system", "content": system_prompt}] + conversations[user_id]["messages"]
        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages = full_messages
        )
        # append assistant response to their list
        assistant_message = response.choices[0].message.content
        conversations[user_id]["messages"].append({"role": "assistant" , "content": assistant_message})

        # return response as json
        return jsonify({
            "user_id": user_id,
            "response": assistant_message,
            "business": business_type,
            "status": "SUCCESS"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# /whatsapp route that accepts POST
@app.route("/whatsapp",methods=['POST'])
def whatsapp_webhook():
    # get user_id and message from request
    data = request.values
    user_input = data.get('Body', '').strip()
    user_id = data.get('From')
    business_type = "coaching"

    if not user_id or not user_input:
        return "Missing user_id or message", 400

    # if user is new, create dict with messages and business_type
    if user_id not in conversations:
        conversations[user_id] = {
            "messages": [],
            "business_type": business_type
        }

    # append user message to their list
    conversations[user_id]["messages"].append({"role": "user", "content": user_input})

    # Look up the business instructions
    system_prompt = SYSTEM_PROMPTS.get(business_type, "You are a helpful assistant")

    # call openai api with their message history
    try:
        full_messages = [{"role": "system", "content": system_prompt}] + conversations[user_id]["messages"]
        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages = full_messages
        )
        # append assistant response to their list
        assistant_message = response.choices[0].message.content
        conversations[user_id]["messages"].append({"role": "assistant" , "content": assistant_message})

        # return response as TwiML
        twilio_response = MessagingResponse()
        twilio_response.message(assistant_message)
        return str(twilio_response)
        
    except Exception as e:
        twilio_response = MessagingResponse()
        twilio_response.message("Error: " + str(e))
        return str(twilio_response)

# /history route that accepts GET
@app.route("/history/<user_id>",methods=['GET'])
def get_history(user_id):
    if user_id in conversations:
        return jsonify({
            "user_id": user_id,
            "history": conversations[user_id]["messages"],
            "business_type": conversations[user_id]["business_type"]
        })
    return jsonify({"error": "User not Found"}),404

# /clear route that accepts POST
@app.route("/clear/<user_id>",methods=['POST'])
def clear_history(user_id):
    if user_id in conversations:
        conversations[user_id]["messages"] = []
        return jsonify({"status": "CLEARED"})
    return jsonify({"error": "User not Found"}),404
    
if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))