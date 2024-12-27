import requests
from bs4 import BeautifulSoup

def scrape_security_news():
    url = "https://example-security-news.com"
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find_all('h2', class_='security-headline')
        return [headline.text for headline in headlines]
    else:
        print(f"Failed to retrieve page: {response.status_code}")
        return []

security_headlines = scrape_security_news()
print('Security Headlines:', security_headlines)
