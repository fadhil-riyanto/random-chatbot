from functions import updateEQ
from flask import Flask, request, jsonify
from predict import predict
from os import getenv

PORT = getenv("PORT") or 3000

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
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(PORT))