from bs4 import BeautifulSoup
import requests
import configuration as conf

html_text = requests.get(conf.urlKommersant, headers=conf.headers).text

soup = BeautifulSoup(html_text, 'lxml')


data = soup.find_all('article', class_='uho rubric_lenta__item js-article')
news_repository = {}


def scraping_news(buff_number):
    id = 0
    for enum_data in data:
        id += 1
        news_repository[id] = {}
        news_headline = enum_data.find('a', class_='uho__link uho__link--overlay').text
        link_to_news = 'https://www.kommersant.ru' + enum_data.find('a', class_='uho__link uho__link--overlay').get('href')
        news_repository[id]["news"] = news_headline
        news_repository[id]["link"] = link_to_news
    return news_repository[buff_number]["news"] + '\n' + news_repository[buff_number]["link"]
