#using url

from WriteIn import writeinmanger
import requests
import threading
import os
import time
from urllib.parse import urlparse

class Dir_Scanner():
    def __init__(self, url, filename):
        self.filename = filename
        self.url = self.Urlparse(url)
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
        self.dic_list = []      #字典名目录
        self.get_url = []       #获取到的所存在的url
        self.get_url_len = 0    #获取到的有效url数量（可重复）
        self.len = 0            #获取到的有效url数量（不重复）
        self.threads_max = self.get_threads()   # 最大线程数
        self.w = writeinmanger()

    def Urlparse(self, url):
        '''
        把传入的url进行截取，只要scheme + netloc部分
        :return:
        '''
        k = urlparse(url)
        l = (k[0] + '://' + k[1])
        return l.rstrip()

    def get_threads(self):
        '''
        取线程数，如果返回为None，则默认50
        '''
        return 50


    def get_dic(self):
        '''
        获取字典目录下的文件名到self.dic_list
        增加把相对路径换成绝对路径的功能
        :return:
        '''
        for root, files, self.dic_list in os.walk('./Burp_force_directory/dictionary'):
            pass

    def more_threads(self):
        self.get_dic()
        #threads = []
        for k in range(0,len(self.dic_list)):
            print(self.dic_list[k])
            self.combine_url(self.dic_list[k])

    def combine_url(self,doc_name):
        '''
        从字典中逐行取出子目录，并将其与传入的网址组合
        '''
        #print(doc_name)
        with open(os.getcwd() + r'\Burp_force_directory\dictionary\\'+doc_name,'r') as file_obj:
            for line in file_obj:
                test_url = self.url + line
                if threading.activeCount() >= self.threads_max:
                    time.sleep(0.7)
                else:
                    t = threading.Thread(target=self.judge, args=(test_url.rstrip(),))
                    t.start()

    def judge(self, test_url):
        '''
        判断所传入的连接是否存在
        '''
        try:
            #print(test_url)
            k = self.request(test_url)
            #print(k.status_code)
            if k.status_code == 200:
                print(test_url)

                if test_url in self.get_url:
                    pass
                else:
                    self.get_url.append(test_url)
                try:
                    #filename = self.url[7:] + '.txt'
                    self.w.writeinfile(self.filename, test_url)
                    self.w.writeinsql_dir(self.filename, test_url)
                    '''
                    这里要把test_url加入到存储位置中
                    '''
                except Exception as e:
                    print(e)
            else:
                #print('##', test_url)
                pass

        except requests.exceptions.Timeout:
            #print('timeout')
            pass
        except Exception as e:
            pass
            #测试模式下开启报错输出
            #print(e)


    def request(self, test_url):
        '''
        用get方法会请求整个【头部+正文】，浪费资源
        利用head方法，只请求【资源头部】
        '''
        r = requests.head(test_url, headers=self.headers, timeout=1)
        return r


if __name__ == '__main__':
    url = 'http://www.baidu.com'
    Web_scanner = Dir_Scanner(url, 'filename')
    Web_scanner.more_threads()
