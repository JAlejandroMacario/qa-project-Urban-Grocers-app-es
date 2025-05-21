import configuration
import requests
import data
from data import kit_body

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())

def get_kit_body():
    return requests.get(configuration.URL_SERVICE + configuration.KITS_PATH,
                        json=kit_body,
                        headers=data.headers)

response = get_kit_body()
print(response.status_code)
print(response.json())

def post_new_client_kit(kit_body):
    headers = data.headers.copy()
    token = post_new_user(data.user_body).json()["authToken"]
    headers["Authorization"] = token
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers)

response = post_new_client_kit(data.kit_body)
print(response.status_code)
print(response.json())
