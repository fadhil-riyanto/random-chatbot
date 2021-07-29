from json import dumps, load
from requester.earthquake import bmkg

def updateEQ():
    print("Updating Earthquake response")
    fl = load(open("intents.json", "r+", encoding="utf-8"))
    for intent in fl["intents"]:
        if intent["tag"] == "gempa":
            data = bmkg()
            intent["responses"] = [f"{data['text']}\nGoogle Map: {data['google_map']}\nShakemap: {data['map']}"]
            print("EQ Updated")
    f = open("intents.json", "r+", encoding="utf-8")
    f.write(dumps(fl, indent=2))