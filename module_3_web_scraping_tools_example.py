
# Python example for Module 3: Python and Web Scraping Tools

# Example of using Requests
import requests
response = requests.get('http://example.com')
print("Content fetched with Requests:\n", response.text[:100], '\n...')

# Example of using BeautifulSoup
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')
print("Title of the page parsed with BeautifulSoup:", soup.title.string)

# Note: Selenium requires a browser driver to be set up, which can't be demonstrated in a simple script file.
