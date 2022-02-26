import psycopg2
from contextlib import closing


class Postgres:
    def insert_into_coins(self, name, ticker):
        with closing(psycopg2.connect(dbname='coingecko_pg', user='postgres',
                                      password='postgres', host='localhost')) as conn:
            with conn.cursor() as cursor:
                cursor.execute("""INSERT INTO coins(name, ticker) VALUES (%s, %s)""", (name, ticker))
                conn.commit()

