import pymssql


class SqlServer:
    """ sqlserver 数据库连接 """
    def __init__(self, host, user, password, database):
        self.cursor = None
        self.conn = None
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        """ 连接数据库 """
        self.conn = pymssql.connect(server=self.host, user=self.user, password=self.password, database=self.database)
        self.cursor = self.conn.cursor()
        return self

    def close(self):
        """ 关闭数据库连接 """
        self.cursor.close()
        self.conn.close()

    def execute(self, sql):
        """ 执行sql语句 """
        self.cursor.execute(sql)
        return self

    def fetchall(self):
        """ 获取所有记录列表 """
        return self.cursor.fetchall()

    def fetchone(self):
        """ 获取一条记录 """
        return self.cursor.fetchone()


__all = ['SqlServer']
