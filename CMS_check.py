#! /usr/bin/env python
#coding=utf-8
#whatweb cms指纹识别api示例
#http://whatweb.bugscaner.com/
#进行json压缩传输,经测试,压缩后可节省将近5-10倍的宽带

import requests
import zlib
import json

class CMS_Check():
    def __init__(self, url):
        self.whatweb("http://" + url)
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
            print(x, ":", request.json()[x][0])

if __name__ == '__main__':
    c = CMS_Check("www.honglian8.com")