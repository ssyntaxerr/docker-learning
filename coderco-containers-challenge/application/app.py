from flask import Flask
import redis
import os

app = Flask(__name__)

# Read Redis connection details from environment variables
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

# Create Redis client
redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)

@app.route("/")
def home():
    return "Welcome to the Flask + Redis app!"

@app.route("/count")
def count():
    # Increment the visit count
    visits = redis_client.incr("visits")
    return f"Visit count: {visits}"

if __name__ == "__main__":
    # Run on all interfaces so Docker can expose it
    app.run(host="0.0.0.0", port=5000, debug=True)
