from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

sensor_data = {}

@app.route('/')
def home():
	return render_template("index.html")

@app.route("/data", methods=["POST"])
def receive_data():
    global sensor_data
    sensor_data = request.get_json()
    print("Received:", sensor_data)
    return jsonify({"status": "ok"})

@app.route("/data", methods=["GET"])
def send_data():
    return jsonify(sensor_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
