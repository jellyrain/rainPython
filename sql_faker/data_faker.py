from faker import Faker
from sql_faker.prizes import one_value_prizes, random_range_prizes

faker_en = Faker()
faker_zh = Faker('zh_CN')


def value_and_null(number: int, value: int | str) -> None | str:
    """ 
    设置返回value的概率 
    :number null 加 value 的总数 
    :value 值
    """
    return value if one_value_prizes([i for i in range(1, number + 1)]) == 1 else None


def is_chinese(chinese: bool) -> Faker:
    """ 是否使用刷的数据是中文 """
    return faker_zh if chinese else faker_en


def name(chinese: bool = True) -> str:
    """ 姓名 """
    return is_chinese(chinese).name()


def name_male(chinese: bool = True) -> str:
    """ 姓名（男） """
    return is_chinese(chinese).name_male()


def name_female(chinese: bool = True) -> str:
    """ 姓名（女） """
    return is_chinese(chinese).name_female()


def msisdn() -> str:
    """ 完整手机号码(加了国家和国内区号) """
    return faker_en.msisdn()


def phone() -> str:
    """ 手机号 """
    return faker_en.phone_number()


def profile(chinese: bool = True) -> dict:
    """ 档案(完整) """
    return is_chinese(chinese).profile()


def simple_profile(chinese: bool = True) -> dict:
    """ 档案(简单) """
    return is_chinese(chinese).simple_profile()


def boolean() -> bool:
    """ 布尔值 """
    return faker_en.pybool()


def ssn(min_age: int = 18, max_age: int = 90) -> str:
    """ 身份证 """
    return faker_zh.ssn(min_age, max_age)


def uuid4() -> str:
    """ uuid4 """
    return faker_en.uuid4()


def job(chinese: bool = True) -> dict:
    """ 职位 """
    return is_chinese(chinese).job()


def email() -> str:
    """ 邮箱 """
    return faker_en.safe_email()


def mac_address() -> str:
    """ mac地址 """
    return faker_en.mac_address()


def ipv4() -> str:
    """ ipv4 """
    return faker_en.ipv4()


def date(pattern: str = "%Y-%m-%d", end_datetime: str = None) -> str:
    """ 日期字符串 """
    return faker_en.date(pattern, end_datetime)


def date_of_birth(tzinfo: str | None = None, minimum_age: int = 0, maximum_age: int = 115):
    """ 出生日期 """
    return faker_en.date_of_birth(tzinfo, minimum_age, maximum_age)


def company(chinese: bool = True) -> str:
    """ 公司名称 """
    return is_chinese(chinese).company()


def address(chinese: bool = True) -> str:
    """ 地址 """
    return is_chinese(chinese).address()


def insert(table_name: str, data: dict[str, str | int]) -> str:
    """ 根据data 生成 insert sql语句 """
    column = ','.join(data.keys())
    value = ','.join([str(item) if type(item) == int else f"'{item}'" for item in data.values()])
    return f'insert into {table_name}({column}) values({value});'


def update(table_name: str, set_data: dict[str, str | int], where_data: dict[str, str | int]) -> str:
    """ 根据data 生成 update sql语句 """
    # return f'update {table_name} set {",".join([ for key, value in set_data.popitem()])};'
