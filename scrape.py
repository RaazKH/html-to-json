import requests
from bs4 import BeautifulSoup
import json

url = input("Enter the URL of the webpage: ")

# Make a GET request to the webpage
response = requests.get(url)

# Parse the HTML content of the webpage using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract all the text from the webpage
text = soup.get_text()

# Create a dictionary to store the data
data = {"url": url, "text": text}

# Write the data to a JSON file
with open("output.json", "w") as f:
    json.dump(data, f)