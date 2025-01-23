# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, ArgoCD! Tôi là Minhyoyo, rất vui được làm quen với bạn"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
