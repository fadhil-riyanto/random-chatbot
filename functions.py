from json import dumps, load
from re import sub
from requester.earthquake import bmkg

def getDownloadUrl(transfer_url):
    parsed_url = sub(r'(http|https)?:\/\/transfer.sh\/', "", transfer_url)
    return f"https://transfer.sh/get/{parsed_url}"

def updateEQ():
    print("Updating Earthquake response")
    fl = load(open("intents.json", "r+", encoding="utf-8"))
    for intent in fl["intents"]:
        if intent["tag"] == "gempa":
            data = bmkg()
            intent["responses"] = [f"{data['text']}\nGoogle Map: {data['google_map']}\nShakemap: {data['map']}"]
            print("EQ Updated")
    f = open("intents.json", "r+", encoding="utf-8")
    f.write(dumps(fl, indent=4))
