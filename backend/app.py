from flask import Flask, redirect, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
    return "hello"


if __name__ == '__main__':
    app.run()