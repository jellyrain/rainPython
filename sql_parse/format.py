import sqlparse


class Keyword_case:
    """ 关键字大小写 """
    lower = 'lower'
    upper = 'upper'
    capitalize = 'capitalize'
    null = None


class Identifier_case:
    """ 标识符大小写 """
    lower = 'lower'
    upper = 'upper'
    capitalize = 'capitalize'
    null = None


class Output_format:
    """ 输出格式 """
    sql = 'sql'
    python = 'python'
    php = 'php'
    null = None


def format_sql(sql: str,
               reindent: bool = True,
               reindent_aligned: bool = False,
               keyword_case: Keyword_case = Keyword_case.null,
               output_format: Output_format = Output_format.sql,
               identifier_case: Identifier_case = Identifier_case.null,
               strip_comments: bool = True,
               strip_whitespace: bool = True,
               indent_width: int = 2,
               indent_columns: bool = False,
               indent_tabs: bool = True,
               use_space_around_operators: bool = True,
               indent_after_first: bool = False,
               comma_first: bool = False) -> str:
    """ 格式化 SQL """
    return sqlparse.format(sql,
                           reindent=reindent,
                           reindent_aligned=reindent_aligned,
                           keyword_case=keyword_case,
                           identifier_case=identifier_case,
                           output_format=output_format,
                           strip_comments=strip_comments,
                           indent_width=indent_width,
                           indent_columns=indent_columns,
                           use_space_around_operators=use_space_around_operators,
                           indent_tabs=indent_tabs,
                           strip_whitespace=strip_whitespace,
                           indent_after_first=indent_after_first,
                           comma_first=comma_first)


def split_sql(sql: str) -> list[str]:
    """ 拆分 SQL """
    return sqlparse.split(sql)


__all__ = ['format_sql', 'split_sql', 'Keyword_case', 'Identifier_case', 'Output_format']
