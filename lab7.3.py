import requests
URL = input("Введите адрес URL: ")
response = requests.get(URL)
print("Ответ от сервера:")
print(response.text)
