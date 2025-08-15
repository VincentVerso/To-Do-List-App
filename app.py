# app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Get the name of the 'version' from an environment variable, default to 'v1'
    version = os.environ.get('APP_VERSION', 'v1.0.0')
    return f'<h1>Hello, World! This is version: {version}</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)