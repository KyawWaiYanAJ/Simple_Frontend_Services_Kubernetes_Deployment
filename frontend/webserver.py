import os
from flask import Flask, redirect

app = Flask(__name__)

# Backend URL from environment variable
BACKEND_URL = os.getenv("BACKEND_URL", "localhost")
BACKEND_PORT = os.getenv("BACKEND_PORT", "5000")

# Port from environment variable, default to 8080 if not set
PORT = int(os.getenv("PORT", 8080))

@app.route("/")
def home():
    return f"""
    <h1>Welcome From Frontend Service</h1>
    <p>Click below to go to Backend Service</p>
    <a href="/redirect">Go to Backend</a>
    """

@app.route("/redirect")
def go_backend():
    return redirect(f"http://{BACKEND_URL}:{BACKEND_PORT}/hello")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
