from flask import Flask, request, jsonify, render_template
from connect_llm import get_rag_response
from db import init_db, save_chat, load_chat
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow JS frontend to access Flask API

# Initialize SQLite DB
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_id = data.get('user_id', 'anonymous')
    user_msg = data.get('user_msg', '').strip()

    if not user_msg:
        return jsonify({'error': 'empty message'}), 400

    try:
        bot_response = get_rag_response(user_msg)

        # Ensure response is a string (not a dict)
        if isinstance(bot_response, dict):
            bot_response = bot_response.get("response", str(bot_response))

        save_chat(user_id, user_msg, bot_response)
        return jsonify({'response': bot_response})
    except Exception as e:
        return jsonify({'Error': str(e)}), 400

@app.route('/history/<user_id>', methods=['GET'])
def history(user_id):
    chats = load_chat(user_id)
    return jsonify([{"user": u, "bot": b} for u, b in chats])

if __name__ == '__main__':
    app.run(debug=True)
