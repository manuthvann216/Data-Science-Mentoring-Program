import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def scrape_images(url):
    # Send an HTTP GET request to the website and retrieve its content
    response = requests.get(url)
    
    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the <img> tags in the parsed HTML and extract the image URLs
    image_urls = [img['src'] for img in soup.find_all('img')]
    
    # Create a directory named 'data' to store the downloaded images
    if not os.path.exists('data'):
        os.makedirs('data')

    # Extract website name and product type from the URL
    parsed_url = urlparse(url)
    website_name = parsed_url.netloc.replace("www.", "")  # Remove 'www' if present
    product_type = parsed_url.path.strip("/")

    # Download and save each image with the website name and product type as the file name
    for url in image_urls:
        response = requests.get(url)
        
        # Extract the image file name from the URL
        file_name = os.path.join('data', f'{website_name}_{product_type}_{url.split("/")[-1]}')

        with open(file_name, 'wb') as file:
            file.write(response.content)
            print(f'Downloaded: {file_name}')


# Prompt the user to enter the website URL
website_url = input('Enter the website URL: ')
scrape_images(website_url)
