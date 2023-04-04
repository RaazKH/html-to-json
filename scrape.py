import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.bahai.org/documents/the-universal-house-of-justice/letter-worlds-religious-leaders'

# Make a request to the website
response = requests.get(url)

# Create a BeautifulSoup object from the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the HTML elements that contain text
elements = soup.find_all(string=True)

# Create a dictionary to store the JSON output
output = {}

# Loop through each element and create a JSON object for it
for index, element in enumerate(elements):
    # Ignore elements that are just whitespace
    if not element.strip():
        continue
    # Ignore elements that are HTML, head, or script tags
    if element.parent.name in ['html', 'head', 'script', 'title', '[document]', 'h6']:
        continue
    if 'class' in element.parent.attrs and ('js-return-top' in element.parent['class'] or 'js-close' in element.parent['class']):
        continue

    # Add the element's JSON object to the output dictionary
    output[f"paragraph{index}"] = element.strip()

# Write the output dictionary to a JSON file
with open('output.json', 'w') as f:
    json.dump(output, f, indent=4, ensure_ascii=False, default=str)
