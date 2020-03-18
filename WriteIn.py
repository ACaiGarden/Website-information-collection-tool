import pymysql

class writeinmanger():
    def __init__(self):
        self.db = pymysql.connect("localhost", "root", "root", "Web_information")

    def writeinfile(self, filename, content):
        filename = filename + '.txt'
        with open(filename, 'a') as f:
            f.write(content + '\n')
            f.close()

    def writeinsql_cms(self, name, item, type):
        cursor = self.db.cursor()
        sql = "INSERT INTO `CMS` (`name`, `item`, `type`) VALUES (%s, %s, %s)"
        try:
            cursor.execute(sql, (name, item, type))
            # 提交到数据库执行
            self.db.commit()
        except:
            self.db.rollback()

    def writeinsql_port(self, name, port, state):
        cursor = self.db.cursor()
        sql = "INSERT INTO `port` (`name`, `port`, `state`) VALUES (%s, %s, %s)"
        try:
            cursor.execute(sql, (name, port, state))
            self.db.commit()
        except:
            self.db.rollback()

    def writeinsql_whois(self, name, item, type):
        cursor = self.db.cursor()
        sql = "INSERT INTO `whois` (`name`, `item`, `type`) VALUES (%s, %s, %s)"
        try:
            cursor.execute(sql, (name, item, type))
            # 提交到数据库执行
            self.db.commit()
        except:
            self.db.rollback()

    def writeinsql_dir(self, name, url):
        cursor = self.db.cursor()
        sql = "INSERT INTO `dir` (`name`, `url`) VALUES (%s, %s)"
        try:
            cursor.execute(sql, (name, url))
            # 提交到数据库执行
            self.db.commit()
        except:
            self.db.rollback()

    def writeinsql_sub(self, name, title, url):
        cursor = self.db.cursor()
        sql = "INSERT INTO `sub` (`name`, `title`, `url`) VALUES (%s, %s, %s)"
        try:
            cursor.execute(sql, (name, title, url))
            # 提交到数据库执行
            self.db.commit()
        except:
            self.db.rollback()

if __name__ =='__main__':
    filename = 'www.qwe.com.txt'
    content = 'qwe/qwe/asdfs.com'
    w = writeinmanger()
    w.writeinfile(filename, content)