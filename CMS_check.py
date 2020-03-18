#! /usr/bin/env python
#coding=utf-8
#using url

import requests
import zlib
import json
import WriteInFile

class CMS_Check():
    def __init__(self, url, filename):
        self.url = "http://" + url
        self.whatweb(self.url)
        self.filename = filename
        self.print_result()

    def whatweb(self, url):
        response = requests.get(url,verify=False)
        #上面的代码可以随意发挥,只要获取到response即可
        #下面的代码您无需改变，直接使用即可
        whatweb_dict = {"url":response.url,"text":response.text,"headers":dict(response.headers)}
        whatweb_dict = json.dumps(whatweb_dict)
        whatweb_dict = whatweb_dict.encode()
        whatweb_dict = zlib.compress(whatweb_dict)
        data = {"info":whatweb_dict}
        return requests.post("http://whatweb.bugscaner.com/api.go",files=data)

    def print_result(self):
        request = self.whatweb("https://aliyun.bugscaner.com")
        print(u"今日识别剩余次数")
        print(request.headers["X-RateLimit-Remaining"])
        print(u"识别结果")
        print(request.json())
        for x in request.json():
            content = x + ":" + request.json()[x][0]
            print(content)
            WriteInFile.WriteIn(self.filename, content)

if __name__ == '__main__':
    c = CMS_Check("www.honglian8.com", "filename.txt")