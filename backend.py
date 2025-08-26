# backend/backend.py
from flask import Flask

app = Flask(__name__)

# Port from environment variable, default to 8080 if not set
PORT = int(os.getenv("PORT", 5000))

@app.route("/hello")
def hello():
    return "Hello from Backend Service!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
