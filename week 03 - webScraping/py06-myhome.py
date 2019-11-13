
# Search for county Mayo properties in https://www.myhome.ie and save price and address from page 1 of the search in a csv file

import requests
import csv
from bs4 import BeautifulSoup
url = "https://www.myhome.ie/residential/mayo/property-for-sale?page=1"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

home_file = open('week03MyHome.csv', mode='w') 
home_writer = csv.writer(home_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

listings = soup.findAll("div", class_="PropertyListingCard" ) # the page source shows the listings are in a containing div with class=” PropertyListingCard”

for listing in listings:
    entryList = []
    
    price = listing.find(class_="PropertyListingCard__Price").text
    entryList.append(price)
    address = listing.find(class_="PropertyListingCard__Address").text
    entryList.append(address)

    home_writer.writerow(entryList)
home_file.close()