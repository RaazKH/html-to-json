import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.bahai.org/documents/the-universal-house-of-justice/letter-worlds-religious-leaders'

# Make a request to the website
r = requests.get(url)

# Create a BeautifulSoup object from the HTML content
soup = BeautifulSoup(r.content, 'html.parser')

# Find all the HTML elements that contain text
elements = soup.find_all(string=True)

# Create a dictionary to store the JSON output
output = {}

# Loop through each element and create a JSON object for it
for element in elements:
    # Ignore elements that are just whitespace
    if not element.strip():
        continue
    # Ignore elements that are HTML, head, or script tags
    if element.parent.name in ['html', 'head', 'script']:
        continue
    if 'class' in element.parent.attrs and ('js-return-top' in element.parent['class'] or 'js-close' in element.parent['class']):
        continue
    # Create a dictionary for the element
    element_dict = {}
    element_dict['text'] = element.strip()
    # Add the element's tag name and attributes to the dictionary
    tag = element.parent.name
    element_dict['tag'] = tag
    attributes = {}
    for attr in element.parent.attrs:
        attributes[attr] = element.parent.attrs[attr]
    element_dict['attributes'] = attributes
    # Add the element's JSON object to the output dictionary
    output[str(element)] = element_dict

# Write the output dictionary to a JSON file
with open('output.json', 'w') as f:
    json.dump(output, f, indent=4, ensure_ascii=False, default=str)
