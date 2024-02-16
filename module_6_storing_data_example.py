
# Example of Storing Scraped Data in CSV and SQLite Database

import csv
import sqlite3

# Sample scraped data
data = [
    {'name': 'Product 1', 'price': '10', 'category': 'Category 1'},
    {'name': 'Product 2', 'price': '15', 'category': 'Category 2'},
]

# Storing data in a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

# Storing data in an SQLite database
conn = sqlite3.connect('scraped_data.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS products (name text, price text, category text)''')
for item in data:
    c.execute('''INSERT INTO products (name, price, category) VALUES (?, ?, ?)''', (item['name'], item['price'], item['category']))
conn.commit()
conn.close()
