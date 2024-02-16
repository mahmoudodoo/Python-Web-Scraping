
# Example of Ethical Web Scraping Practices

import requests
import time
from urllib.robotparser import RobotFileParser

# URL to scrape
url = 'http://example.com'

# Checking robots.txt
robots_url = 'http://example.com/robots.txt'
rp = RobotFileParser()
rp.set_url(robots_url)
rp.read()
if not rp.can_fetch('*', url):
    print("Scraping blocked by robots.txt")
else:
    # Implementing rate limiting
    time.sleep(1)  # Simple example of rate limiting
    response = requests.get(url)
    # Process the response
    print("Content fetched:", response.text[:100])
