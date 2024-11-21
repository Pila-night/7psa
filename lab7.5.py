import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse, urljoin

def get_full_url(base_url, relative_url):
    parsed_base_url = urlparse(base_url)
    if relative_url.startswith('http://') or relative_url.startswith('https://'):
        return relative_url
    if relative_url.startswith('/'):
        return f"{parsed_base_url.scheme}://{parsed_base_url.netloc}{relative_url}"
    return urljoin(base_url, relative_url)

def save_images_from_url(url, save_directory, visited_urls):
    if url in visited_urls:
        return
    visited_urls.add(url)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    images = soup.find_all('img')
    for image in images:
        image_url = image['src']
        full_image_url = get_full_url(url, image_url)  
        
        image_data = requests.get(full_image_url).content
        image_name = full_image_url.split('/')[-1]
        file_path = os.path.join(save_directory, image_name)

        if not os.path.exists(file_path):
            with open(file_path, 'wb') as f:
                f.write(image_data)        
            print(f"Загружено изображение: {image_name}")
        else:
            print(f"Изображение уже существует: {image_name}")

    links = soup.find_all('a', href=True)
    for link in links:
        link_url = link['href']
        full_link_url = get_full_url(url, link_url)  
        save_images_from_url(full_link_url, save_directory, visited_urls)

URL = input("Введите URL страницы: ")
save_directory = input("Введите путь к директории для сохранения изображений: ")
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

visited_urls = set()
save_images_from_url(URL, save_directory, visited_urls)

print("Изображения успешно загружены!")
