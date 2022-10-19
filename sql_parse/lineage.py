import json
from sqllineage.core.models import Column, Table
from sqllineage.runner import LineageRunner


class column_parse:
    """ 解析 column """
    def __init__(self, column: Column) -> None:
        self.__database = None
        self.__table_name = None
        self.__source = None
        self.__column = column
        self.__column_parent = column.parent
        self.__column_name = column.raw_name
        self.__table_type = column.parent.__class__.__name__
        self.table_judgment()

    def table_judgment(self) -> None:
        """ 判断表类型 """
        if self.__column.parent:
            if type(self.__column.parent) == Table:
                self.__table_name = self.__column_parent.raw_name
                self.__database = self.__column_parent.schema
            else:
                self.__table_name = self.__column_parent.alias
                self.__database = None
        else:
            self.__table_name = 'Unknown'
            self.__database = None

    def dict(self) -> dict[str, str | None]:
        """ 返回一个字典 """
        return {
            'column_name': str(self.__column_name),
            'table_name': str(self.__table_name),
            'table_type': str(self.__table_type),
            'database': str(self.__database),
            'source': self.__source
        }

    def json(self) -> str:
        """ 返回一个 json """
        return json.dumps(self.dict())


def column_lineage(columns: tuple[Column, ...]) -> dict[str, str | None]:
    """ 单字段血缘 """
    data = None
    current = None
    for column in reversed(columns):
        if data is None:
            data = column_parse(column).dict()
            current = data
        else:
            current['source'] = column_parse(column).dict()
            current = current['source']
    return data


def table_lineage(sql: str) -> list[dict[str, str | None]]:
    """ 表级血缘 """
    data = []
    for columns in LineageRunner(sql).get_column_lineage():
        data.append(column_lineage(columns))
    return data


__all__ = ['table_lineage']
