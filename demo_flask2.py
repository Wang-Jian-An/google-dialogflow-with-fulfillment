from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask 2"

if __name__ == "__main__":
    app.run()