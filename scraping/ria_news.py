from bs4 import BeautifulSoup
import requests
import configuration as conf

html_text = requests.get(conf.urlRIA, headers=conf.headers).text

soup = BeautifulSoup(html_text, 'lxml')

data = soup.find_all('div', class_='list-item')
news_repository = {}


def scraping_news(buff_number):
    id = 0
    for enum_data in data:
        id += 1
        news_repository[id] = {}
        news_headline = enum_data.find('a', class_='list-item__title color-font-hover-only').text
        link_to_news = enum_data.find('a', itemprop='url').get('href')
        news_repository[id]["news"] = news_headline
        news_repository[id]["link"] = link_to_news
    return news_repository[buff_number]["news"] + '\n' + news_repository[buff_number]["link"]

