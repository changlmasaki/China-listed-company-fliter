import time
from urllib.parse import urlencode
import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd


def get_one_page(i):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
        }
        paras = {
            'reportTime': '2021-12-31',
            'pageNum': i
        }
        url = 'https://s.askci.com/stock/a/0-0?' + urlencode(paras)
        print(url)
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
    except requests.exceptions.RequestException:
        print('FAILED')


def parse_one_page(html):
    # soup = BeautifulSoup(html, features="html.parser")
    # tr_list = soup.find_all('tbody')
    # print(tr_list)
    # for data in tr_list:
    # sub_data = data.text.split()
    # print(sub_data)

    tb1 = pd.read_html(html, header=0)[3]
    #print(tb1["股票代码"])
    tb1["股票代码"] = tb1["股票代码"].astype(str)
    tb1["股票代码"] = tb1["股票代码"].str.zfill(6)
    return tb1


def save_csv(data):
    df = pd.concat(data)
    df.to_csv(r'C:\Users\chang\Desktop\table\上市公司信息.csv', index=False)


def main(page):
    data = []
    for i in range(1, page + 1):
        web_data = get_one_page(i)
        time.sleep(5)
        tb = parse_one_page(web_data)
        data.append(tb)
    save_csv(data)


if __name__ == '__main__':
    main(100)
