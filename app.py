#!flask/bin/python
from flask import Flask, render_template, jsonify, request, abort
from transferwise import Transferwise
from env import API_CLIENT_KEY
import asyncio, env

# Init Flask application
app = Flask(__name__)

# Init Transferwise API
tw = Transferwise(API_CLIENT_KEY)

# Home page routing
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Run the app
if __name__ == "__main__":
    app.jinja_env.cache = {}
    app.run()