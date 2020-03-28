import socket

from Port_scanner import NmPortScanner
from Burp_force_directory import Dir_Scanner
from Who_is import WhoIs
from Subdomain_search import Subdomain
from CMS_check import CMS_Check
from sensitive_file import sensitive_file_scanner

import argparse
import pymysql
from configparser import ConfigParser

class main():
    def __init__(self, url):
        self.domain = url
        self.ipaddress = self.get_domain_to_ip(self.domain)
        self.filename = self.get_filename(self.domain)
        print(self.domain, ":", self.ipaddress)

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

    '''
    def commend_parse(self):
        parser = argparse.ArgumentParser(description="information collecting tool")

        parser.add_argument('-d', '--dir', action='store_true', help="Burp force directory")
        parser.add_argument('-p', '--port', action='store_true', help="Port scan")
        parser.add_argument('-w', '--whois', action='store_true', help="Get whois information")
        parser.add_argument('-c', '--cms', action='store_true', help="Get CMS type")
        parser.add_argument('-s', '--sub', action='store_true', help="Search subdomain")
        parser.add_argument('-u', '--url', help="Please input without 'http://'")

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
        else:
            print("please input the url.")
    '''

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
        c = CMS_Check(self.domain, self.filename)

    def get_file(self):
        s = sensitive_file_scanner(self.domain, self.filename)
        s.scanner()


class main_sql():
    def __init__(self, db):
        self.db = db
    '''
    def login(self):
        cfg = ConfigParser()
        cfg.read('config.ini')
        username = cfg.get('mysql', 'username')
        password = cfg.get('mysql', 'password')
        try:
            connection = pymysql.connect("localhost", username, password, "Web_information")
            print("Connect success!")
            return connection
        except:
            print("Connect false!")
            while True:
                # 输入账号密码，直到成功登录。
                username = input("Please input the username:")
                password = input("Please input the password:")
                try:
                    connection = pymysql.connect("localhost", username, password, "Web_information")
                    print("Connect success!")
                    cfg.set('mysql', 'username', username)
                    cfg.set('mysql', 'password', password)
                    with open('config.ini', 'w') as c:
                        cfg.write(c)
                    return connection
                except:
                    print("error")
    '''
    '''
    def command_parse(self):
        parser = argparse.ArgumentParser(description="information database!")
        group = parser.add_mutually_exclusive_group()
        group.add_argument("-s", "--search", help="search information from the database")
        group.add_argument("-d", "--delete", help="delete information from the database")
        args = parser.parse_args()

        if args.search:
            self.search(args.search)
        if args.delete:
            self.delete(args.delete)
    '''

    def search(self, name):
        cursor = self.db.cursor()
        sql_commend = []
        sql_commend.append("SELECT * FROM cms WHERE name='%s'"%name)
        sql_commend.append("SELECT * FROM port WHERE name='%s'"%name)
        sql_commend.append("SELECT * FROM whois WHERE name='%s'"%name)
        sql_commend.append("SELECT * FROM dir WHERE name='%s'"%name)
        sql_commend.append("SELECT * FROM sub WHERE name='%s'"%name)

        for commend in sql_commend:
            cursor.execute(commend)
            result = cursor.fetchall()
            print("=" * 60)
            for x in result:
                print(x)
        print("=" * 60)

    def delete(self, name):
        cursor = self.db.cursor()
        sql_commend = []
        sql_commend.append("DELETE FROM cms WHERE name='%s'" % name)
        sql_commend.append("SELECT * FROM port WHERE name='%s'" % name)
        sql_commend.append("SELECT * FROM whois WHERE name='%s'" % name)
        sql_commend.append("SELECT * FROM dir WHERE name='%s'" % name)
        sql_commend.append("SELECT * FROM sub WHERE name='%s'" % name)

        for commend in sql_commend:
            cursor.execute(commend)
        print("Delete finished.")

def login():
    cfg = ConfigParser()
    cfg.read('config.ini')
    username = cfg.get('mysql', 'username')
    password = cfg.get('mysql', 'password')
    try:
        connection = pymysql.connect("localhost", username, password, "Web_information")
        print("Connect success!")
        return connection
    except:
        print("Connect false!")
        while True:
            # 输入账号密码，直到成功登录。
            username = input("Please input the username:")
            password = input("Please input the password:")
            try:
                connection = pymysql.connect("localhost", username, password, "Web_information")
                print("Connect success!")
                cfg.set('mysql', 'username', username)
                cfg.set('mysql', 'password', password)
                with open('config.ini', 'w') as c:
                    cfg.write(c)
                return connection
            except:
                print("error")

def choose():
    db = login()    #return a database connection.
    parser = argparse.ArgumentParser(description="information collecting tool")

    parser.add_argument('-d', '--dir', action='store_true', help="Burp force directory")
    parser.add_argument('-p', '--port', action='store_true', help="Port scan")
    parser.add_argument('-w', '--whois', action='store_true', help="Get whois information")
    parser.add_argument('-c', '--cms', action='store_true', help="Get CMS type")
    parser.add_argument('-s', '--sub', action='store_true', help="Search subdomain")
    parser.add_argument('-f', '--file', action='store_true', help="Sensitive file")
    parser.add_argument('-u', '--url', help="Please input without 'http://'")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-S", "--search", help="search information from the database")
    group.add_argument("-D", "--delete", help="delete information from the database")

    args = parser.parse_args()
    if args.url:
        m = main(args.url)
        if args.dir:
            m.get_dir()
        if args.port:
            m.get_port()
        if args.whois:
            m.get_whois()
        if args.cms:
            m.get_cms()
        if args.sub:
            m.get_subdomain()
        if args.file:
            m.get_file()
    elif not args.url and (args.dir or args.port or args.whois or args.sub or args.cms):
        print("please input the url!")
    if args.search:
        msql = main_sql(db)
        msql.search(args.search)
    if args.delete:
        msql = main_sql(db)
        msql.delete(args.delete)


if __name__ == '__main__':
    choose()            #选择扫描界面或数据库界面

    #m = main()