from bs4 import BeautifulSoup
import requests
import configuration as conf

html_text = requests.get(conf.urlSportru, headers=conf.headers).text

soup = BeautifulSoup(html_text, 'lxml')

data = soup.find_all('div', class_='short-news')
news_repository = {}


def scraping_news(buff_number):
    id = 0
    for enum_data in data:
        id += 1
        news_repository[id] = {}
        news_headline = enum_data.find('a', class_='short-text').text
        link_to_news = 'https://www.sports.ru' + enum_data.find('a', class_='short-text').get('href')
        news_repository[id]["news"] = news_headline
        news_repository[id]["link"] = link_to_news
    return news_repository[buff_number]["news"] + '\n' + news_repository[buff_number]["link"]