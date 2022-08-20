import sqlite3


class Db_Api:

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def close_db(self):
        self.cursor.close()
        self.conn.close()

    def create_table(self, table_name: str, table_columns: dict) -> None:
        """
        创建表
        :param table_name: 表名
        :param table_columns: 列名和类型
        :return:
        """
        sql = 'CREATE TABLE IF NOT EXISTS ' + table_name + '('
        for key in table_columns:
            sql += key + ' ' + table_columns[key] + ','
        sql = sql[:-1] + ')'
        self.cursor.execute(sql)
        self.conn.commit()

    def insert_data(self, table_name: str, data: dict) -> None:
        """
        插入数据
        :param table_name: 表名
        :param data: 数据
        :return:
        """
        sql = 'INSERT INTO ' + table_name + ' VALUES('
        for key in data:
            sql += '"' + data[key] + '",'
        sql = sql[:-1] + ')'
        self.cursor.execute(sql)
        self.conn.commit()

    def select_data(self, table_name: str, condition: dict) -> list:
        """
        查询数据
        :param table_name: 表名
        :param condition: 查询条件
        :return:
        """
        sql = 'SELECT * FROM ' + table_name + ' WHERE '
        for key in condition:
            sql += key + '="' + condition[key] + '" AND '
        sql = sql[:-5]
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def update_data(self, table_name: str, condition: dict, data: dict) -> None:
        """
        更新数据
        :param table_name: 表名
        :param condition: 查询条件
        :param data: 更新数据
        :return:
        """
        sql = 'UPDATE ' + table_name + ' SET '
        for key in data:
            sql += key + '="' + data[key] + '",'
        sql = sql[:-1] + ' WHERE '
        for key in condition:
            sql += key + '="' + condition[key] + '" AND '
        sql = sql[:-5]
        self.cursor.execute(sql)
        self.conn.commit()

    def delete_data(self, table_name: str, condition: dict) -> None:
        """
        删除数据
        :param table_name: 表名
        :param condition: 查询条件
        :return:
        """
        sql = 'DELETE FROM ' + table_name + ' WHERE '
        for key in condition:
            sql += key + '="' + condition[key] + '" AND '
        sql = sql[:-5]
        self.cursor.execute(sql)
        self.conn.commit()

    def drop_table(self, table_name: str) -> None:
        """
        删除表
        :param table_name: 表名
        :return:
        """
        sql = 'DROP TABLE ' + table_name
        self.cursor.execute(sql)
        self.conn.commit()

    def create_index(self, table_name: str, index_name: str, index_columns: list) -> None:
        """
        创建索引
        :param table_name: 表名
        :param index_name: 索引名
        :param index_columns: 索引列名
        :return:
        """
        sql = 'CREATE INDEX ' + index_name + ' ON ' + table_name + '('
        for column in index_columns:
            sql += column + ','
        sql = sql[:-1] + ')'
        self.cursor.execute(sql)
        self.conn.commit()

    def drop_index(self, index_name: str) -> None:
        """
        删除索引
        :param index_name: 索引名
        :return:
        """
        sql = 'DROP INDEX ' + index_name
        self.cursor.execute(sql)
        self.conn.commit()


__all__ = ['Db_Api']
