# argv[1]:search target, argv[2]:amount of images

import os
import sys
import json
import urllib
import requests
from bs4 import BeautifulSoup


class Google:
    def __init__(self):
        self.GOOGLE_SEARCH_URL = 'https://www.google.co.jp/search'
        self.session = requests.session()
        self.session.headers.update(
            {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'})

    def search(self, keyword, maximum):
        print('searching images :', keyword)
        query = self.query_gen(keyword)
        return self.image_search(query, maximum)

    def query_gen(self, keyword):
        # 検索クエリジェネレータ
        page = 0
        while True:
            params = urllib.parse.urlencode({
                'q': keyword,
                'tbm': 'isch',
                'ijn': str(page)})

            yield self.GOOGLE_SEARCH_URL + '?' + params
            page += 1

    def image_search(self, query_gen, maximum):
        # 画像検索
        result = []
        total = 0
        while True:
            # 検索
            html = self.session.get(next(query_gen)).text
            soup = BeautifulSoup(html, 'lxml')
            elements = soup.select('.rg_meta.notranslate')
            jsons = [json.loads(e.get_text()) for e in elements]
            imageURLs = [js['ou'] for js in jsons]

            # 検索結果の追加
            if not len(imageURLs):
                print('-> no more images')
                break
            elif len(imageURLs) > maximum - total:
                result += imageURLs[:maximum - total]
                break
            else:
                result += imageURLs
                total += len(imageURLs)

        print('-> finally got', str(len(result)), 'images')
        return result


if __name__ == '__main__':
    google = Google()
    if len(sys.argv) != 3:
        print('invalid argment')
        sys.exit()
    else:
        # 保存先
        data_dir = 'data/'
        os.makedirs(data_dir, exist_ok=True)
        os.makedirs('data/' + sys.argv[1], exist_ok=True)
        # 画像検索
        result = google.search(
            sys.argv[1], maximum=int(sys.argv[2]))

        for i in range(len(result)):
            print('-> downloading image', i+1)
            urllib.request.urlretrieve(
                result[i], 'data/' + sys.argv[1] + '/' + str(i+1) + '.jpg')
