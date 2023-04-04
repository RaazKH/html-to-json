import requests
from bs4 import BeautifulSoup
import json

url = input("Enter the URL of the webpage: ")

# Make a GET request to the webpage
response = requests.get(url)

# Parse the HTML content of the webpage using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract all the text from the webpage and split it by newlines when it's enclosed in its own container
sections = []
for index, element in enumerate(soup.find_all('p')):
    html_content = str(element)
    sections.append({f"text{index+1}": html_content})

# Write the data to a formatted JSON file
with open("output.json", "w") as f:
    json.dump(sections, f, indent=4, ensure_ascii=False, default=str)
