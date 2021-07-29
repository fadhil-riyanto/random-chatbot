import requests
from json import dumps
from re import sub

def getDownloadUrl(transfer_url):
    parsed_url = sub(r'(http|https)?:\/\/transfer.sh\/', "", transfer_url)
    return f"https://transfer.sh/get/{parsed_url}"

# URL
url_gempa = "https://gist.githubusercontent.com/hansputera/5c76ee8b784fc2fa232923fa1208be35/raw/e3a26c79199695af124220f63c3ea0e1ea0db3f7/dataset-gempa.json"
url_dataset1 = "https://gist.githubusercontent.com/hansputera/0c10e5a76a136a1c177df8214cf65388/raw/2a5d8b5bb8306ba3fac96aa26dcbf1c9ec8e2e09/datasets1.json"
url_dataset2 = "https://transfer.sh/15ZCZUp/telegram_anonymouschatgroupdua.json"
url_dataset3 = "https://transfer.sh/1tQ2RSs/telegram_anonymousgroupchatsatu.json"

# Importing gempa
print("Downloading gempa dataset")
response = requests.get(url_gempa)
open("datasets1/custom_gempa.json", "w+").write(dumps(response.json()))
print("Completed gempa dataset")

# Importing dataset 1 
print("Downloading dataset 1")
response = requests.get(url_dataset1)
open("datasets1/telegram_anonymouschatgroupbaru.json", "w+").write(dumps(response.json()))
print("Completed dataset 1")

# Importing dataset 2
print("Downloading dataset 2")
response = requests.get(getDownloadUrl(url_dataset2))
open("datasets1/telegram_anonymouschatgroupdua.json", "w+").write(dumps(response.json()))
print("Completed dataset 2")

# Importing dataset 3
print("Downloading dataset 3")
response = requests.get(getDownloadUrl(url_dataset3))
open("datasets1/telegram_anonymouschatgroupsatu.json", "w+").write(dumps(response.json()))
print("Completed dataset 3")