import requests
from bs4 import BeautifulSoup
import os

URL = input("Введите URL страницы: ")
save_directory = input("Введите путь к директории для сохранения изображений: ")
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

images = soup.find_all('img')
for image in images:
    image_url = image['src']
    
    if not image_url.startswith('http'):
        image_url = URL + image_url
    
    image_data = requests.get(image_url).content
    image_name = image_url.split('/')[-1]
    file_path = os.path.join(save_directory, image_name)

    with open(file_path, 'wb') as f:
        f.write(image_data)

print("Изображения успешно загружены!")

