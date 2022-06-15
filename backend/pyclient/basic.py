import requests

# endpoint = "http://httpbin.org/status/200"
# endpoint = "http://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api"

# Http Request
get_reponse = requests.get(endpoint, params={"abc":123}, json = {"query":"Hello World"}) # Application Programming Interference

# Http Reponse
print(get_reponse.json()["message"])
print(get_reponse.status_code)