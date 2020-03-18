import pymysql

class SQLmanger():
    def __init__(self):
        self.db = pymysql.connect("localhost", "root", "root", "Web_information")

    def insert_CMS(self, item, type):
        cursor = self.db.cursor()
        # SQL 插入语句
        sql = "INSERT INTO `port` (`item`, `type`) VALUES (%s, %s)"
        try:
           # 执行sql语句
           cursor.execute(sql, (item, type))
           # 提交到数据库执行
           self.db.commit()
        except:
           # 如果发生错误则回滚
           self.db.rollback()
        # 关闭数据库连接
        self.db.close()