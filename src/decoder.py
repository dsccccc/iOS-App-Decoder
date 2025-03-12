import requests
import argparse
from bs4 import BeautifulSoup

free = b'\xf0\x9f\x86\x93'.decode('UTF-8')


class AppStore:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--url', type=str, required=True)
        parser.add_argument('--note', type=str, default=' app.')
        args = parser.parse_args()

        self.HEADERS = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; TAS-AN00 Build/HUAWEITAS-AN00; wv) "
                                      "AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.61 Mobile "
                                      "Safari/537.36 Super 4.6.5"}
        self.url: str = args.url
        self.note: str = args.note
        self.content: str = ''

    def crawler(self):
        response = requests.get(self.url, headers=self.HEADERS)
        assert response.status_code == 200
        soup = BeautifulSoup(response.text, from_encoding='utf-8', features="html.parser")
        h1 = soup.find('h1')
        head = h1.get_text().replace(h1.find('span').get_text(), '').strip(' ')
        # for div in soup.find('div'):
        #     for _ in div.findAll('h2'):
        #         for info in div.find('dl').findAll('div'):
        #             if 'Price' in info.text:
        #                 price = info.text.replace('Price', '')
        self.content = f'[{head}]({self.url}) {free} {self.note}'
