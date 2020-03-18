#using IP

import requests
from urllib import parse
from bs4 import BeautifulSoup
from WriteIn import writeinmanger

class Subdomain():
    def __init__(self, address, filename):
        self.address = address
        self.filename = filename
        self.w = writeinmanger()

    def get_Web(self):
        header = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36'
                                ' (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
        result = requests.get('https://cn.bing.com/search?q=ip:' + self.address, headers = header)
        print(result.url)
        #print(result.text)
        soup = BeautifulSoup(result.text, 'html.parser')
        all_a = soup.find_all('a', target="_blank", class_="", id="")
        for x in all_a:
            print(x['href'])
            print(x.string)
            content = "[" + x.string + "]:" + x['href']
            self.w.writeinfile(self.filename, content)
            self.w.writeinsql_sub(self.filename, x.string, x['href'])

if __name__ == '__main__':
    s = Subdomain('183.232.231.172', 'filename')
    s.get_Web()