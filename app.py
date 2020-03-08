#!flask/bin/python
from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap
from transferwise import Transferwise
import env

# Init Flask application
app = Flask(__name__)

# Init Bootstrap App
bootstrap = Bootstrap(app)

# Init Transferwise API class
tw = Transferwise(env.API_KEY)

# Home page routing
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Run the app
if __name__ == "__main__":
    app.run(debug=True)