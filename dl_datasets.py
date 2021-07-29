import requests
from json import dumps
from functions import getDownloadUrl

# URL
url_others = "https://transfer.sh/1cxqi7W/custom_others.json"
url_greetings = "https://transfer.sh/1938RTf/custom_greetings.json"
url_gempa = "https://gist.githubusercontent.com/hansputera/5c76ee8b784fc2fa232923fa1208be35/raw/e3a26c79199695af124220f63c3ea0e1ea0db3f7/dataset-gempa.json"
url_dataset1 = "https://gist.githubusercontent.com/hansputera/0c10e5a76a136a1c177df8214cf65388/raw/2a5d8b5bb8306ba3fac96aa26dcbf1c9ec8e2e09/datasets1.json"
url_dataset2 = "https://transfer.sh/15ZCZUp/telegram_anonymouschatgroupdua.json"
url_dataset3 = "https://transfer.sh/1tQ2RSs/telegram_anonymousgroupchatsatu.json"
url_dataset4 = "https://transfer.sh/1tCqRBd/telegram_englishchatz.json"

# Importing greetings
print("Downloading greetings dataset")
response = requests.get(url_greetings)
open("datasets/greetings.json", "w+").write(dumps(response.json()))
print("Completed greetings dataset")

# Importing others
print("Downloading others dataset")
response = requests.get(url_others)
open("datasets/others.json", "w+").write(dumps(response.json()))
print("Completed others dataset")

# Importing gempa
print("Downloading gempa dataset")
response = requests.get(url_gempa)
open("datasets/custom_gempa.json", "w+").write(dumps(response.json()))
print("Completed gempa dataset")

# Importing dataset 1 
print("Downloading dataset 1")
response = requests.get(url_dataset1)
open("datasets/telegram_anonymouschatgroupbaru.json", "w+").write(dumps(response.json()))
print("Completed dataset 1")

# Importing dataset 2
print("Downloading dataset 2")
response = requests.get(getDownloadUrl(url_dataset2))
open("datasets/telegram_anonymouschatgroupdua.json", "w+").write(dumps(response.json()))
print("Completed dataset 2")

# Importing dataset 3
print("Downloading dataset 3")
response = requests.get(getDownloadUrl(url_dataset3))
open("datasets/telegram_anonymouschatgroupsatu.json", "w+").write(dumps(response.json()))
print("Completed dataset 3")

# Importing dataset 4
print("Downloading dataset 4")
response = requests.get(getDownloadUrl(url_dataset4))
open("datasets/telegram_englishchatz.json", "w+").write(dumps(response.json()))
print("Completed dataset 4")