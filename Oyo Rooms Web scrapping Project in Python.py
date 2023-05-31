#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install beautifulsoup4


# In[4]:


pip install requests


# In[6]:


import requests
from bs4 import BeautifulSoup
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('oyo_hotels.db')
c = conn.cursor()

# Create a table to store the hotel information
c.execute('''CREATE TABLE IF NOT EXISTS hotels
             (name TEXT, price TEXT, rating TEXT)''')

# Send a GET request to the OYO Rooms website
url = 'https://www.oyorooms.com/hotels-in-bangalore/'
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the hotel listings on the page
hotel_listings = soup.find_all('div', class_='oyo-row')

# Extract information from each hotel listing and store it in the database
for listing in hotel_listings:
    name = listing.find('h3', class_='listingHotelDescription__hotelName').text.strip()
    price = listing.find('span', class_='listingPrice__finalPrice').text.strip()
    rating = listing.find('span', class_='hotelRating__ratingSummary').text.strip()

    # Insert the extracted data into the database
    c.execute("INSERT INTO hotels (name, price, rating) VALUES (?, ?, ?)", (name, price, rating))

# Commit the changes and close the database connection
conn.commit()
conn.close()

