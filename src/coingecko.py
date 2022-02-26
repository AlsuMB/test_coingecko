from bs4 import BeautifulSoup
import requests
from pycoingecko import CoinGeckoAPI


# cg = CoinGeckoAPI()
# url = 'https://www.coingecko.com/ru'
# print(cg.get_coins_list())
from src.postgres import Postgres


class CoinGecko:
    def insert_data_into_coins_table(self):
        for coin in self.all_coins:
            postgres = Postgres()
            print(coin['id'], coin['symbol'])
            postgres.insert_into_coins(coin['name'], coin['symbol'])

    def insert_data_into_exchanges_table(self):
        pass

    def __init__(self):
        self.cg = CoinGeckoAPI()
        self.all_coins = self.cg.get_coins_list()


c = CoinGecko()
c.insert_data_into_coins_table()
