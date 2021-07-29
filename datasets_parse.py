import re
from os import listdir
from json import dumps, load
from config import maximalArrayItem, ignored_texts
from functions import updateEQ

source = "datasets"
intents = []

def patternOrResponse(num):
    return "pattern" if num % 2 == 0 else "response"

regrex_pattern = re.compile(pattern = "["
                        u"\U0001F600-\U0001F64F"  # emoticons
                        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                        u"\U0001F680-\U0001F6FF"  # transport & map symbols
                        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)

for fl in listdir(source):
    if fl.endswith(".json"):
        if fl.startswith("telegram"):
             file = load(open(f"{source}/{fl}", "r+", encoding="utf8"))
             patterns = []
             responses = []

             messages = file["messages"]
             index = 1
             for message in messages:
                 if type(message["text"]) == str and len(message["text"]) > 0:
                    message["text"] = regrex_pattern.sub(r"", message["text"]).strip()
                    if len(message["text"]) > 2 and message["text"].lower() not in ignored_texts:
                        if len(patterns) < maximalArrayItem and patternOrResponse(index) == "pattern":
                            patterns.append(message["text"].lower())
                        elif len(responses) < maximalArrayItem and patternOrResponse(index) == "response":
                            responses.append(message["text"].lower())
                 index += 1
             tagName = fl.split("_")[1].split(".")[0]
             intents.append({"tag": tagName, "patterns": list(dict.fromkeys(patterns)), "responses": list(dict.fromkeys(responses)), "context": []})
             print(f"{tagName} intent loaded. Parsing {len(messages)} messages to {len(patterns)} patterns, and {len(responses)} responses")
        elif fl.startswith("custom"):
            file = load(open(f"{source}/{fl}", "r+", encoding="utf8"))
            patterns = []
            for message in file["messages"]:
                if len(message) > 0:
                    if len(patterns) < maximalArrayItem:
                        patterns.append(message.lower())
            tagName = fl.split("_")[1].split(".")[0]
            intents.append({"tag": tagName, "patterns": list(dict.fromkeys(patterns)), "responses": file.get("responses", []), "context": file.get("context", [])})
            print(f"{tagName} intent loaded, {len(patterns)} patterns")

print("Saving intents to intents.json")
with open("intents.json", "r+") as f:
    f.write(dumps({"intents": intents}, indent=4))
    updateEQ()
    print("Intents saved")