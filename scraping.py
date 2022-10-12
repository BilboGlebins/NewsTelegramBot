from bs4 import BeautifulSoup
import requests
import configuration as conf

html_text = requests.get(conf.urlRIA, headers=conf.headers).text

soup = BeautifulSoup(html_text, 'lxml')

data = soup.find_all('div', class_='list-item')

for enum_data in data:
    news_headline = enum_data.find('a', class_='list-item__title color-font-hover-only').text
    link_to_news = enum_data.find('a', itemprop='url').get('href')

    print(news_headline + '\n' + link_to_news + '\n')













