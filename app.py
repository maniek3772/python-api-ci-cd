# app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({"message": "Hello, World!"})

@app.route('/health')
def health_check():
    return jsonify({"status": "ok"})

@app.route('/echo/<name>')
def echo(name):
    return jsonify({"message": f"Hello, {name}!"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
