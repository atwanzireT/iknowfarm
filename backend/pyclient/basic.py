import requests

# endpoint = "http://httpbin.org/status/200"
endpoint = "http://httpbin.org/anything"

# Http Request
get_reponse = requests.get(endpoint, json = {"query":"Hello World"}) # Application Programming Interference

# Http Reponse
# print(get_reponse.text)
print(get_reponse.status_code)