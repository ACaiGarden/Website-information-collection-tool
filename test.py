import pymysql
from configparser import ConfigParser
import argparse

class main_sql():
    def __init__(self):
        self.db = self.login()

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

    def command_parse(self):
        parser = argparse.ArgumentParser(description="information database!")
        


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


if __name__ == "__main__":
    m = main_sql()
    #m.search('filename.txt')
    #m.delete('filename.txt')
    #m.login()