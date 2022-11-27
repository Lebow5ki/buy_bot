import requests, json
import urllib.request
import pandas as pd
import threading


def request():
    print('1')
    def get_url():
        webURL = requests.get('https://market.csgo.com/itemdb/current_730.json').text
        data = json.loads(webURL)
        return data['db']

    def get_file(data):
        destination = 'item.csv'
        URL = 'https://market.csgo.com/itemdb/' + str(data)
        urllib.request.urlretrieve(URL, destination)

    def edit_file():
        r = pd.read_csv('item.csv', sep=';')
        df = pd.DataFrame(r)
        df = df.drop(df.columns[[4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16]],axis=1)  # Удаляем по номеру столбца (начиная с 0)
        df = df.drop(labels=[1], axis=0)# Удаляем по номеру строки (начиная с 0)
        df.to_csv('out.csv', index=False, header=None)

    data = get_url()
    get_file(data)
    edit_file()


threading.Timer(5.0, request).start()


