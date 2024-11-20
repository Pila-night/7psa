import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

def download_images_from_page(url, visited):
    if url in visited:
        return 

    visited.add(url)  
    print(f"Загружаем страницу: {url}")

    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки HTTP

        soup = BeautifulSoup(response.text, 'html.parser')
        os.makedirs('images', exist_ok=True)

        images = soup.find_all('img')
        for img in images:
            img_url = img.get('src')
            if img_url:
                img_url = urljoin(url, img_url)  
                img_name = os.path.join('images', os.path.basename(img_url))

                try:
                    img_response = requests.get(img_url)
                    img_response.raise_for_status()  # Проверка на ошибки HTTP при загрузке изображения
                    
                    with open(img_name, 'wb') as f:
                        f.write(img_response.content)
                    print(f"Сохранено: {img_name}")
                except requests.exceptions.RequestException as e:
                    print(f"Ошибка при загрузке изображения: {img_url} - {e}")

        links = soup.find_all('a', href=True)
        for link in links:
            link_url = link['href']
            link_url = urljoin(url, link_url) 
            download_images_from_page(link_url, visited) 

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при загрузке страницы: {e}")

start_url = "https://best-stroi.ru/"
visited_urls = set()  
download_images_from_page(start_url, visited_urls)
