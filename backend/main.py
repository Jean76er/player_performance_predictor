from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restful import Api

app = Flask(__name__)
CORS(app)
api = Api(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/data", methods=['GET'])
def get_data():
    test_message = "This endpoint just sent you a message"

    return jsonify({"message": test_message})

@app.route("/test", methods=['POST'])
def test():
    data = request.get_json()
    return jsonify({
        "message": "Backend received data!",
        "data": data
    })

if __name__ == "__main__":
    app.run(port=8000, debug=True)