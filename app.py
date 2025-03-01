from flask import Flask, request, jsonify


app = Flask(__name__)

export FLASK_APP=app.py
export FLASK_ENV=development
export FLASK_DEBUG=1
export FLASK_PORT=5000


@app.route('/')
def hello():
    return 'Hello, Flask!'