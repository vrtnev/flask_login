from flask import Flask
from flask_login import UserMixin

app = Flask(__name__)

@app.route('/')
def index():
    return "hello"

if __name__ == "__main__":
    app.run(debug=True