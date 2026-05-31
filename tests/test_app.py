from flask import Flask, jsonify
import time

app = Flask(__name__)

time_request_count = 0


@app.get("/time")
def get_time():
    global time_request_count

    time_request_count += 1

    return jsonify({"time": int(time.time())})


@app.get("/metrics")
def get_metrics():
    return jsonify({"count": time_request_count})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)