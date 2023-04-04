import requests
from bs4 import BeautifulSoup
import json

url = input("Enter the URL of the webpage: ")

# Make a GET request to the webpage
response = requests.get(url)

# Parse the HTML content of the webpage using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')


# Extract all the text from the webpage within <p> tags
sections = []
for index, element in enumerate(soup.find_all('p')):
    text = element.decode_contents().strip()
    # Remove the first and last <p> tags and strip whitespace
    if text.startswith('<p>'):
        text = text[3:]
    if text.endswith('</p>'):
        text = text[:-4]
    text = text.strip()
    sections.append({f"text{index+1}": text})


# Write the data to a formatted JSON file
with open("output.json", "w") as f:
    json.dump(sections, f, indent=4, ensure_ascii=False, default=str)
