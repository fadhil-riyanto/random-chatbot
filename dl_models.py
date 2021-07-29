import requests
from functions import getDownloadUrl

url_pkl = "https://transfer.sh/1LcpLkO/data.pkl"
url_model = "https://transfer.sh/1gry1Vi/tensor_model.h5"

# Importing pickle file
print("Downloading pickle data")
r = requests.get(getDownloadUrl(url_pkl), allow_redirects=True)
open('models/data.pkl', 'wb+').write(r.content)
print("Completed pickle")

# Importing tensor
print("Downloading tensor model")
r = requests.get(getDownloadUrl(url_model), allow_redirects=True)
open('models/tensor_model.h5', 'wb+').write(r.content)
print("Completed tensor")
