import psycopg2
from psycopg2 import Error

from configuration import name_db, user_db, password_db, host_db


def create_table_users(buff_cursor):
    create_table = '''CREATE TABLE users
                      (id_user UUID PRIMARY KEY     NOT NULL,
                      username VARCHAR    NOT NULL); '''
    buff_cursor.execute(create_table)
    connection.commit()
    print('Table "users" successfully created')


def drop_table_users(buff_cursor):
    drop_table = 'DROP TABLE users'
    buff_cursor.execute(drop_table)
    connection.commit()
    print('Table "users" deleted successfully')


def create_table_sourse(buff_cursor):
    create_table = '''CREATE TABLE sourse
                      (id_sourse UUID PRIMARY KEY     NOT NULL,
                      sourse VARCHAR    NOT NULL); '''
    buff_cursor.execute(create_table)
    connection.commit()
    print('Table "sourse" successfully created')


def drop_table_sourse(buff_cursor):
    drop_table = 'DROP TABLE sourse'
    buff_cursor.execute(drop_table)
    connection.commit()
    print('Table "sourse" deleted successfully')


def create_table_user_actions(buff_cursor):
    create_table = '''CREATE TABLE user_actions
                                   (id_action UUID PRIMARY KEY     NOT NULL,
                                   id_user UUID     NOT NULL,
                                   action VARCHAR    NOT NULL,
                                   FOREIGN KEY (id_user) REFERENCES users (id_user)); '''
    buff_cursor.execute(create_table)
    connection.commit()
    print('Table "user_actions" successfully created')


def drop_table_user_actions(buff_cursor):
    drop_table = 'DROP TABLE user_actions'
    buff_cursor.execute(drop_table)
    connection.commit()
    print('Table "user_actions" deleted successfully')


def create_table_news(buff_cursor):
    create_table = '''CREATE TABLE news
                      (id_news UUID PRIMARY KEY     NOT NULL,
                      id_source UUID     NOT NULL,
                      header VARCHAR    NOT NULL,
                      link VARCHAR    NOT NULL,
                      FOREIGN KEY (id_source) REFERENCES sourse (id_sourse)); '''
    buff_cursor.execute(create_table)
    connection.commit()
    print('Table "news" successfully created')


def drop_table_news(buff_cursor):
    drop_table = 'DROP TABLE news'
    buff_cursor.execute(drop_table)
    connection.commit()
    print('Table "news" deleted successfully')


def create_table_subscriptions(buff_cursor):
    create_table = '''CREATE TABLE subscriptions
                      (id_subscription UUID PRIMARY KEY     NOT NULL,
                      id_user UUID     NOT NULL,
                      id_source UUID     NOT NULL,
                      FOREIGN KEY (id_user) REFERENCES users (id_user),
                      FOREIGN KEY (id_source) REFERENCES sourse (id_sourse)); '''
    buff_cursor.execute(create_table)
    connection.commit()
    print('Table "subscriptions" successfully created')


def drop_table_subscriptions(buff_cursor):
    drop_table = 'DROP TABLE subscriptions'
    buff_cursor.execute(drop_table)
    connection.commit()
    print('Table "subscriptions" deleted successfully')


try:
    connection = psycopg2.connect(host=host_db,
                                  user=user_db,
                                  password=password_db,
                                  database=name_db)

    cursor = connection.cursor()

    #create_all_table = create_table_users(cursor), \
    #                   create_table_sourse(cursor), \
    #                   create_table_user_actions(cursor), \
    #                   create_table_news(cursor), \
    #                   create_table_subscriptions(cursor)

    #drop_all_table = drop_table_subscriptions(cursor), \
    #                 drop_table_news(cursor), \
    #                 drop_table_user_actions(cursor),  \
    #                 drop_table_sourse(cursor), \
    #                 drop_table_users(cursor)


except (Exception, Error) as error:
    print(f'[INFO] Error while working with PostgreSQL: {error}')
finally:
    if connection:
        cursor.close()
        connection.close()
        print('PostgreSQL connection closed')
