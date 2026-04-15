from dotenv import load_dotenv
from openai import OpenAI
from flask import Flask, request, jsonify
import os
import json

load_dotenv()

# create flask app\
app = Flask(__name__)

# create openai client using env variable
client = OpenAI(
    api_key = os.getenv("API_KEY"),
    base_url = "https://openrouter.ai/api/v1"
)
# empty conversations dictionary
conversations = {}

# /chat route that accepts POST
@app.route("/chat",methods=['POST'])
def user_info():

# get user_id and message from request
    data = request.json
    user_id = data.get('user_id')
    user_input = data.get('message')

    if not user_id or not user_input:
        return jsonify({"error": "Missing user_id or message"}), 400

# if user is new, create empty list for them
    if user_id not in conversations:
        conversations[user_id] = []

# append user message to their list
    conversations[user_id].append({"role": "user", "content": user_input})

# call openai api with their message history
    try:
        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages = conversations[user_id]
        )
# append assistant response to their list
        assistant_message = response.choices[0].message.content
        conversations[user_id].append({"role": "assistant" , "content": assistant_message})

# return response as json
        return jsonify({
            "user_id": user_id,
            "response": assistant_message,
            "status": "SUCCESS"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# /history route that accepts GET
@app.route("/history/<user_id>",methods=['GET'])
def get_history(user_id):
    if user_id in conversations:
        return jsonify({
            "user_id": user_id,
            "history": conversations[user_id]
        })
    return jsonify({"error": "User not Found"}),404

# /clear route that accepts POST
@app.route("/clear/<user_id>",methods=['GET'])
def clear_history(user_id):
    if user_id in conversations:
        conversations[user_id] = []
        return jsonify({"status": "CLEARED"})
    return jsonify({"error": "User not Found"}),404
    
if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))