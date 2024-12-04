from flask import Flask, jsonify, request

app = Flask(__name__)

# Define a simple route
@app.route('/')
def home():
    return "Welcome to the MY Flask API!"

# Define an API endpoint
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello, Flask!", "data": [1, 2, 3]})

# Define a POST endpoint
@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.json
    return jsonify({"message": "Data received!", "data": data}), 201

if __name__ == '__main__':
    app.run(debug=True)
