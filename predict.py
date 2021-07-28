import pickle
import tensorflow as tf
import pandas as pd
from util import bow, words
from main import classes, random
import math
from json import load

intents = load(open("intents.json", "rb"))
data = pickle.load(open("models/data.pkl", "rb"))
global graph
graph = tf.compat.v1.get_default_graph()
model = tf.keras.models.load_model("models/tensor_model.h5")

def classify_local(sentence):
    ERROR_THRESHOLD = 0.25
    input_data = pd.DataFrame([bow(sentence, words)], dtype=float, index=["input"])
    results = model.predict(input_data)[0]
    results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append((classes[r[0]], str(r[1])))
    return return_list

def predict_score(sentence):
    ERROR_THRESHOLD = 0.25
    input_data = pd.DataFrame([bow(sentence, words)], dtype=float, index=["input"])
    results = model.predict([input_data])[0]
    results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getRandomInt(min, max):
    return math.floor(random.randint(min, max))

def predict(sentence):
    global intents
    intents = intents["intents"] if type(intents) != list else intents
    predict_scores = predict_score(sentence)
    msg = None
    ctx = None
    for intent in intents:
        if intent["tag"] == predict_scores[0]["intent"]:
            respId = getRandomInt(0, len(intent["responses"])-1)
            msg = intent["responses"][respId]
            ctx = intent["context"][0] if len(intent["context"]) > 0 else None
            break
    return { "msg": msg.strip(), "ctx": ctx }
