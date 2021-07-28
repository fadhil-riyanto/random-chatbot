from functions import updateEQ
from flask import Flask, request, jsonify
from predict import predict

app = Flask("ChatBOT")
@app.route("/", methods=["POST"])
def olahChat():
    data = request.json
    if data == None or data.get("text", None) == None:
        return jsonify({"status": "error", "message": "No text"})
    else:
        result = predict(data["text"])
        return jsonify(result)

@app.route("/reload-earthquake")
def reloadEQ():
    updateEQ()
    return jsonify({"status": "success"})

app.run("0.0.0.0", 3000)