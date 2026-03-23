"""
Sample app for Guardian testing.
Uses flask, requests, numpy — all defined in requirements.txt
"""

import flask
import requests
import numpy as np


app = flask.Flask(__name__)


@app.route("/")
def home():
    return {"status": "ok", "message": "Guardian test app running"}


@app.route("/compute")
def compute():
    # Simple numpy operation to test numpy works
    arr = np.array([1, 2, 3, 4, 5])
    return {
        "mean":  float(np.mean(arr)),
        "sum":   float(np.sum(arr)),
        "array": arr.tolist()
    }


@app.route("/ping")
def ping():
    # Simple requests usage
    try:
        r = requests.get("https://httpbin.org/get", timeout=3)
        return {"status": r.status_code, "message": "external call ok"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


if __name__ == "__main__":
    app.run(debug=True, port=5000)
