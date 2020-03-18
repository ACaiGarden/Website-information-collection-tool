#using url
import requests
from bs4 import BeautifulSoup
from WriteIn import writeinmanger

class WhoIs():
    def __init__(self, url, filename):
        self.filename = filename
        self.url = 'http://whois.chinaz.com/' + url
        #self.get_Web()
        self.w = writeinmanger()

    def get_Web(self):
        r = requests.get(self.url)
        #print(r.text)
        soup = BeautifulSoup(r.text, 'html.parser')
        #for x in range(13, len(soup.find_all("span"))):
        #    print(soup.find_all("span")[x].string)
        '''
        for x in soup.find_all("div", class_="fl WhLeList-left"):
            print(x.string)
        for x in soup.find_all("div", class_="fr WhLeList-right"):
            try:
                print(x.string)
            except:
                pass
        
        for x, y in soup.find_all("div", class_="fl WhLeList-left"), soup.find_all("div", class_="fr WhLeList-right"):
            try:
                print(x.string, y.string)
            except:
                pass
        '''
        try:
            x = soup.find("ul", class_="WhoisLeft")
            #print(x)
            y = x.find_all("li")
            for k in y:
                try:
                    div_content = k.find_all("div")
                    print(div_content[0].string)
                    print(div_content[1].span.string)
                    content = div_content[0].string + ':' + div_content[1].span.string
                    self.w.writeinfile(self.filename, content)
                    self.w.writeinsql_whois(self.filename, div_content[0].string, div_content[1].span.string)
                except:
                    pass
        except:
            print("Whois:该域名被屏蔽")
            self.w.writeinfile(self.filename, "Whois:该域名被屏蔽")


if __name__ == '__main__':
    w = WhoIs("www.honglian8.com/index.asp", 'filename')
    w.get_Web()