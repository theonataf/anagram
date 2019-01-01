import psycopg2


def connect():
    return psycopg2.connect(user='postgres', password='tafna1313',
                            database='word-games', host='localhost')
