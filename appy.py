from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/app")
def home():
    return jsonify({"message": "Hello World, API is working!"})
@app.route("/appy")
def home():
    a="hi"
    return jsonify({"key":a,"jock":"JICK"})

if __name__ == "__main__":

    app.run(host='0.0.0.0',debug=True)



