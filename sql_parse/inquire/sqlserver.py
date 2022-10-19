from sql_parse.inquire.dbconnect import SqlServer
from sql_parse.format import format_sql


def get_all_database(sqlserver: SqlServer) -> list[str]:
    """ 获取 sqlserver 数据库中全部数据库 """
    sql = "SELECT NAME FROM MASTER.DBO.SYSDATABASES ORDER BY NAME"
    return [i[0] for i in sqlserver.connect().execute(sql).fetchall()]


def get_object(sqlserver: SqlServer, xtype: str) -> str:
    """ 获取 sqlserver 数据库中对象的定义 """
    sql = f"SELECT NAME FROM SYSOBJECTS WHERE XTYPE='{xtype}' ORDER BY NAME"
    return [item[0] for item in sqlserver.connect().execute(sql).fetchall()]


def get_all_table(sqlserver: SqlServer) -> list[str]:
    """ 获取 sqlserver 数据库中全部表 """
    return get_object(sqlserver, "U")


def get_column_table(sqlserver: SqlServer, table_name: str) -> list[dict[str, str]]:
    """ 获取 sqlserver 数据库中表的字段 """
    sql = f"SELECT COLUMN_NAME, ORDINAL_POSITION, IS_NULLABLE, DATA_TYPE, CHARACTER_OCTET_LENGTH FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}'"
    return [{
        "column_name": i[0],
        "ordinal_position": i[1],
        "is_nullable": i[2],
        "data_type": i[3],
        "character_octet_length": i[4]
    } for i in sqlserver.connect().execute(sql).fetchall()]


def get_pk_table(sqlserver: SqlServer, table_name: str) -> list[str]:
    """ 获取 sqlserver 数据库中表的主键 """
    sql = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE WHERE TABLE_NAME = '{table_name}'"
    return [i[0] for i in sqlserver.connect().execute(sql).fetchall()]


def get_all_view(sqlserver: SqlServer) -> list[str]:
    """ 获取 sqlserver 数据库中全部视图 """
    return get_object(sqlserver, "V")


def get_all_function(sqlserver: SqlServer) -> list[str]:
    """ 获取 sqlserver 数据库中全部函数 """
    return get_object(sqlserver, "FN") + get_object(sqlserver, "IF") + get_object(sqlserver, "TF")


def get_all_user(sqlserver: SqlServer) -> list[str]:
    """ 获取 sqlserver 数据库中全部用户 """
    sql = "SELECT NAME FROM SYSUSERS"
    return [i[0] for i in sqlserver.connect().execute(sql).fetchall()]


def get_all_procedure(sqlserver: SqlServer) -> list[str]:
    """ 获取 sqlserver 数据库中全部存储过程 """
    return get_object(sqlserver, "P")


def get_all_trigger(sqlserver: SqlServer) -> list[str]:
    """ 获取 sqlserver 数据库中全部触发器 """
    return get_object(sqlserver, "TR")


def get_table_ddl(sqlserver: SqlServer, table_name: str) -> str:
    """ 获取 sql server 一张表的 ddl 语句 """
    sql = f"""
select 'create table [' + so.name + '] (' + o.list + ')' + CASE
                                                                       WHEN tc.Constraint_Name IS NULL THEN ''
                                                                       ELSE 'ALTER TABLE ' + so.Name +
                                                                            ' ADD CONSTRAINT ' + tc.Constraint_Name +
                                                                            ' PRIMARY KEY ' +
                                                                            ' (' + LEFT(j.List, Len(j.List)-1) + ')' END
        from sysobjects so
            cross apply
            (SELECT
            '  ['+ column_name +'] ' +
            data_type + case data_type
            when 'sql_variant' then ''
            when 'text' then ''
            when 'ntext' then ''
            when 'xml' then ''
            when 'image' then ''
            when 'decimal' then '(' + cast (numeric_precision as varchar) + ', ' + cast (numeric_scale as varchar) + ')'
            else coalesce ('('+ case when character_maximum_length = -1 then 'MAX' else cast (character_maximum_length as varchar) end +')', '') end + ' ' +
            case when exists (
            select id from syscolumns
            where object_name(id)=so.name
            and name = column_name
            and columnproperty(id, name, 'IsIdentity') = 1
            ) then
            'IDENTITY(' +
            cast (ident_seed(so.name) as varchar) + ',' +
            cast (ident_incr(so.name) as varchar) + ')'
            else ''
            end + ' ' +
            (case when IS_NULLABLE = 'No' then 'NOT ' else '' end ) + 'NULL ' +
            case when information_schema.columns.COLUMN_DEFAULT IS NOT NULL THEN 'DEFAULT '+ information_schema.columns.COLUMN_DEFAULT ELSE '' END + ', '
            from information_schema.columns where table_name = so.name
            order by ordinal_position
            FOR XML PATH ('')) o (list)
            left join
            information_schema.table_constraints tc
        on tc.Table_name = so.Name
            AND tc.Constraint_Type = 'PRIMARY KEY'
            cross apply
            (select '[' + Column_Name + '], '
            FROM information_schema.key_column_usage kcu
            WHERE kcu.Constraint_Name = tc.Constraint_Name
            ORDER BY
            ORDINAL_POSITION
            FOR XML PATH ('')) j (list)
        where xtype = 'U'
          AND name = '{table_name}'    
"""
    return format_sql(sqlserver.connect().execute(sql).fetchone()[0])


def get_fptv_sql(sqlserver: SqlServer, name: str) -> str:
    """ 获取 sql server 一个 函数，存储过程，触发器，视图 的 ddl 语句 """
    sql = f"sp_helptext '{name}'"
    result = ''
    for item in sqlserver.connect().execute(sql).fetchall():
        if item[0].strip() != '':
            result += item[0]
    return result


__all__ = ['get_all_database', 'get_all_table', 'get_column_table', 'get_pk_table', 'get_all_view', 'get_all_function',
           'get_all_user', 'get_all_procedure', 'get_all_trigger', 'get_table_ddl', 'get_fptv_sql']
