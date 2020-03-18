#using IP

import requests
from urllib import parse
from bs4 import BeautifulSoup
import WriteInFile

class Subdomain():
    def __init__(self, address, filename):
        self.address = address
        self.filename = filename

    def get_Web(self):
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
        result = requests.get('https://cn.bing.com/search?q=ip:' + self.address, headers = header)
        print(result.url)
        print(result.text)
        soup = BeautifulSoup(result.text, 'html.parser')
        all_a = soup.find_all('a', target="_blank", class_="", id="")
        for x in all_a:
            print(x['href'])
            print(x.string)
            content = "[" + x.string + "]:" + x['href']
            WriteInFile.WriteIn(self.filename, content)

if __name__ == '__main__':
    s = Subdomain('183.232.231.172', 'filename.txt')
    s.get_Web()