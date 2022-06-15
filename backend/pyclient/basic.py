import requests

endpoint = "http://httpbin.org/status/200"
endpoint = "http://httpbin.org/anything"

# Http Request
get_reponse = requests.get(endpoint) # Application Programming Interference

# Http Reponse
print(get_reponse.text)