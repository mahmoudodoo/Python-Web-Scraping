
# Practical Web Scraping with BeautifulSoup Example

import requests
from bs4 import BeautifulSoup

# Making an HTTP request to fetch the web page content
url = 'http://example.com'
response = requests.get(url)

# Parsing the HTML content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Example of extracting data: Fetching the title of the web page
page_title = soup.title.text
print("Page Title:", page_title)

# Example of finding a specific element and extracting data
first_paragraph = soup.find('p').text
print("First paragraph text:", first_paragraph)
