from flask import Flask
import redis
import os

# Read the environment variables (with defaults)
redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", 6379))

# Connect to Redis
r = redis.Redis(host=redis_host, port=redis_port)

app = Flask(__name__)

@app.route("/")
def count():
    r.incr("hits")
    return f"Hits: {r.get('hits').decode()}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)

