
# Python example for Module 2: The Basics of HTML and CSS
# This example demonstrates parsing HTML with BeautifulSoup

from bs4 import BeautifulSoup

# Sample HTML content
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Page Title</title>
</head>
<body>
<h1>This is a Heading</h1>
<p>This is a paragraph.</p>
</body>
</html>
"""

# Parsing the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Extracting the title of the page
page_title = soup.title.text
print("Page Title:", page_title)

# Extracting the heading
heading = soup.h1.text
print("Heading:", heading)

# Extracting the paragraph
paragraph = soup.p.text
print("Paragraph:", paragraph)
