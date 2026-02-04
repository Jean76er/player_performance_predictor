from flask import Flask, jsonify
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/data", methods=['GET'])
def get_data():
    test_message = "This endpoint just sent you a message"

    return jsonify({"message": test_message})

if __name__ == "__main__":
    app.run(debug=True)