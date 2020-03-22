import socket

from Port_scanner import NmPortScanner
from Burp_force_directory import Dir_Scanner
from Who_is import WhoIs
from Subdomain_search import Subdomain
from CMS_check import CMS_Check

import argparse
import pymysql


class main():
    def __init__(self):
        self.commend_parse()
        #self.domain = input("Please input the domain(Without 'http://'):")#目标网址
        #self.ipaddress = self.get_domain_to_ip(self.domain)    #由目标网址得到的IP地址
        #self.filename = self.get_filename(self.domain)  #从目标网址提取关键词做文件名

    def get_domain_to_ip(self, domain):
        '''
        这里往后可以加正则表达式
        '''
        try:
            ip_addr = socket.getaddrinfo(domain, 'http')
            #print(ip_addr[0][4][0])
            return ip_addr[0][4][0]
        except:
            print('Failed domain!')

    def get_filename(self, url):
        result = url.split('.')
        for x in result:
            if x != 'www':
                name = x
                break
        else:
            name = 'None_name'
        return name

    def commend_parse(self):
        parser = argparse.ArgumentParser(description="information collecting tool")

        parser.add_argument('-d', '--dir', action='store_true', help="Burp force directory")
        parser.add_argument('-p', '--port', action='store_true', help="Port scan")
        parser.add_argument('-w', '--whois', action='store_true', help="Get whois information")
        parser.add_argument('-c', '--cms', action='store_true', help="Get CMS type")
        parser.add_argument('-s', '--sub', action='store_true', help="Search subdomain")
        parser.add_argument('url', help="Please input without 'http://'")

        args = parser.parse_args()
        if args.url:
            self.domain = args.url
            self.ipaddress = self.get_domain_to_ip(self.domain)
            self.filename = self.get_filename(self.domain)
            print(self.domain, ":", self.ipaddress)
        if args.dir:
            self.get_dir()
        if args.port:
            self.get_port()
        if args.whois:
            self.get_whois()
        if args.cms:
            self.get_cms()
        if args.sub:
            self.get_subdomain()


    def get_dir(self):
        address = 'http://' + str(self.domain)
        d = Dir_Scanner(address, self.filename)
        d.more_threads()

    def get_port(self):
        n = NmPortScanner(self.ipaddress, self.filename)
        n.scan()
        n.print_result()

    def get_whois(self):
        w = WhoIs(self.domain, self.filename)
        w.get_Web()

    def get_subdomain(self):
        s = Subdomain(self.ipaddress, self.filename)
        s.get_Web()

    def get_cms(self):
        c = CMS_Check(self.domain, self.ipaddress)


class main_sql():
    def __init__(self):
        self.db = pymysql.connect("localhost", "root", "root", "Web_information")

    def search(self, name):
        cursor = self.db.cursor()
        sql = "SELECT * FROM "

    def delete(self, name):
        pass

if __name__ == '__main__':
    m = main()