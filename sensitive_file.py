import requests
import os
from WriteIn import writeinmanger
import threading
import time
'''
result = requests.get('http://127.0.0.1:8080/123.zip')
print(result.content)
with open('333.zip', 'wb') as file:
    file.write(result.content)
'''


class sensitive_file_scanner():
    def __init__(self, url, filename):
        self.url = 'http://' + url
        self.filename = filename
        self.dirlist = self.get_dir_list()
        self.w = writeinmanger()
        self.threads_max = 50

    def get_dir_list(self):
        filelist = []
        filePath = '.\\Sensitive_file_directory'
        for i, j, filelist in os.walk(filePath):
            pass
        return filelist

    def scanner(self):
        for file in self.dirlist:
            with open(os.getcwd() + r'\Sensitive_file_directory\\' + file,'r') as file_obj:
                for line in file_obj:
                    line = line.strip('\n')
                    test_url = self.url + line
                    #self.check(test_url, line)
                    while threading.activeCount() >= self.threads_max:
                        time.sleep(0.1)
                    t = threading.Thread(target=self.check, args=(test_url, line, ))
                    t.start()


    def check(self, test_url, save_file_name):
        try:
            k = requests.get(test_url, timeout=1)
            if k.status_code == 200 and len(k.content) != 0:
                #print(test_url)
                try:
                    with open('.\\Sensitive_file\\' + save_file_name, 'wb') as file:
                        file.write(k.content)
                    print(test_url)
                    self.w.writeinfile(self.filename, test_url)
                    self.w.writeinsql_file(self.filename, test_url)
                    '''
                    这里要把test_url加入到存储位置中
                    '''
                except Exception as e:
                    pass
            else:
                pass
        except:
            pass

if __name__ == '__main__':

    url = 'www.baidu.com'
    filename = 'baidu'
    s = sensitive_file_scanner(url, filename)
    s.scanner()
    '''
    re = requests.get('http://127.0.0.1:8080/123.txt')
    print(re.status_code)
    print(re.content)
    with open('.\\Sensitive_file\\' + '/123.txt', 'wb') as file:
        file.write(re.content)
    '''
