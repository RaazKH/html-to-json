# HTML to JSON

This Python script takes a URL for a webpage as an input and then takes all the text of that page and outputs it to a JSON file.

## Usage

To use the script, run it from the command line and enter the URL of the webpage you want to scrape when prompted:

```
python scrape.py
Enter the URL of the webpage: [Enter URL here]
```

The script will then extract all the text from the webpage and output it to a file named `output.json`.

## Dependencies

The script requires the following Python libraries:

- `requests`
- `beautifulsoup4`

You can install these libraries using `pip`:

```
pip install requests beautifulsoup4

```

## How it works

The script works as follows:

1. Prompt the user to enter the URL of the webpage they want to scrape.
2. Use the `requests` library to make a GET request to the URL and get the HTML content of the webpage.
3. Use the `BeautifulSoup` library to parse the HTML content and extract all the text from the webpage.
4. Create a dictionary to store the data we want to output to the JSON file. This dictionary contains the URL of the webpage and the text of the webpage.
5. Use the `json` library to write the data to a JSON file named `output.json`.