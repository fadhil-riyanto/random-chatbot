import requests

url_pkl = "https://transfer.sh/1JV9QmM/data.pkl"
url_model = "https://transfer.sh/14SHDgA/tensor_model.h5"

# Importing pickle file
print("Downloading pickle data")
r = requests.get(url_pkl, allow_redirects=True)
open('models/data.pkl', 'wb+').write(r.content)
print("Completed pickle")

# Importing tensor
print("Downloading tensor model")
r = requests.get(url_model, allow_redirects=True)
open('models/tensor_model.h5', 'wb+').write(r.content)
print("Completed tensor")
