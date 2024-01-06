from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

messages = []

@app.route('/messages', methods=['GET', 'POST'])
def chat():
    global messages
    if request.method == 'POST':
        content = request.json
        messages.append(content)
        return jsonify({"status": "OK"})
    else:
        return jsonify(messages)

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app
