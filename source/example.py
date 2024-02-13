import requests
from bs4 import BeautifulSoup

def get_news_headlines(url):
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headlines = soup.find_all('h3', class_='headline')
    
    for headline in headlines:
        print(headline.text.strip())

url = input("Enter the website URL to scrape headlines from: ")

get_news_headlines(url)
