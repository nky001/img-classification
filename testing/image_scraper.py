import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import hashlib

# Function to download images from a webpage
def download_images(url, folder_path):
    # Define headers to request higher quality images
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    # Send an HTTP request to the URL with the specified headers
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all image tags
        img_tags = soup.find_all('img')
        
        # Download and save each image
        for img_tag in img_tags:
            # Get the image source URL
            img_url = img_tag.get('src')
            
            # Join the base URL and the image URL to get the absolute URL
            img_url = urljoin(url, img_url)
            
            # Get the filename part of the URL
            img_filename = hashlib.sha1(img_url.encode()).hexdigest() + ".png"
            
            # Save the image to the specified folder
            img_filepath = os.path.join(folder_path, img_filename)
            
            # Send a request to the image URL with headers
            img_response = requests.get(img_url, headers=headers)
            
            with open(img_filepath, 'wb') as img_file:
                img_file.write(img_response.content)
                print(f"Image saved: {img_filepath}")
    else:
        print(f"Failed to fetch webpage. Status code: {response.status_code}")

# Example usage
webpage_url = 'import os'
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import hashlib

# Function to download images from a webpage
def download_images(url, folder_path):
    # Define headers to request higher quality images
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    # Send an HTTP request to the URL with the specified headers
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all image tags
        img_tags = soup.find_all('img')
        
        # Download and save each image
        for img_tag in img_tags:
            # Get the image source URL
            img_url = img_tag.get('src')
            
            # Join the base URL and the image URL to get the absolute URL
            img_url = urljoin(url, img_url)
            
            # Get the filename part of the URL
            img_filename = hashlib.sha1(img_url.encode()).hexdigest() + ".png"
            
            # Save the image to the specified folder
            img_filepath = os.path.join(folder_path, img_filename)
            
            # Send a request to the image URL with headers
            img_response = requests.get(img_url, headers=headers)
            
            with open(img_filepath, 'wb') as img_file:
                img_file.write(img_response.content)
                print(f"Image saved: {img_filepath}")
    else:
        print(f"Failed to fetch webpage. Status code: {response.status_code}")

# Example usage
webpage_url = 'https://www.gettyimages.in/photos/rohit-shetty?assettype=image&family=editorial&phrase=rohit%20shetty&sort=mostpopular'
download_folder = r"C:\Users\Lenovo\Documents\data science\image-classification\images\rohit_shetty"

# Create the download folder if it doesn't exist
os.makedirs(download_folder, exist_ok=True)

# Call the download_images function
download_images(webpage_url, download_folder)

