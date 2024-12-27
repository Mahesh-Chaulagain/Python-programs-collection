import requests
from bs4 import BeautifulSoup

# load the newspaper website to scrap the information about the current exchange rate
URL = 'https://www.lanacion.com.ar/'
page = requests.get(URL)

# parse the HTML data
soup = BeautifulSoup(page.content, "html.parser")
# use select to find an element in DOM
span = soup.select('a[title="Dólar blue"] span')[0]
price = span.get_text()

print(price)

