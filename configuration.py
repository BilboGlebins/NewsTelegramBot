from decouple import config

#Токен бота
botToken = config('token', default='')

#Данные для связи с БД
name_db = config('database', default='')
user_db = config('user', default='')
password_db = config('password', default='')
host_db = config('host', default='')



#Заголовок, который браузеры отправляют в запросах на идентификацию
headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5(.NET CLR 3.5.30729)"}

#URL новостных сайтов
urlRIA = 'https://ria.ru/lenta'
urlRBC = 'https://www.rbc.ru/short_news'
urlKommersant = 'https://www.kommersant.ru/lenta'
urlSportru = 'https://www.sports.ru/news/'

#Число для вывода новостей по умолчанию
amt_news = 5

#Текст сообщений выводимых ботом
textStart = '''Здравствуйте! 
Я бот для отображения новостей из источников, чтобы вы всегда были в курсе того, что происходит в мире.
            
Расскажу, что я умею:
/from_source – команда для получения списка источников новостей и возможностью выбора списка новостей из источника.
/update_n – команда для изменения количества отображаемых новостей, которые я могу вам показать за раз.
/subscribe – команда для подписки на источник новостей
'''

testSourse = '''Выберите источник'''

textUpdate = '''Данная функция изменяет количество отображаемых новостей.
(по умолчанию 5, не более 10)
Введите число отображаемых новостей: '''

textPassUpdate = '''Значение изменено'''

textErrorUpdate = '''Введено неверное значение'''

testSubscribe = '''Выберите источник на который хотите подписаться'''
testSubscribeDone = '''Вы подписались на источник'''







