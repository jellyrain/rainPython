import random
import uuid


class Id_Type:
    NUMBER = '0123456789'
    ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ALPHANUMERIC = ALPHABET + NUMBER
    SPECIAL = '!@#$%^&*()_+=-[]{};:,./<>?|'
    ALL = ALPHANUMERIC + SPECIAL
    ALPHABET_UPPER_SPECIAL = ALPHABET.upper() + SPECIAL
    ALPHABET_LOWER_SPECIAL = ALPHABET.lower() + SPECIAL
    NUMBER_SPECIAL = NUMBER + SPECIAL


# 随机数类型
ID_TYPE = Id_Type()


def random_id(length: int = 8, id_type: str = ID_TYPE.ALPHANUMERIC) -> str:
    """
    随机生成ID
    :param length: 长度
    :param id_type: 类型
    :return:
    """
    return ''.join(random.sample(id_type, length))


def uuid_v1() -> str:
    """
    生成uuidv1
    :return:
    """
    return str(uuid.uuid1())


def uuid_v4() -> str:
    """
    生成uuidv4
    :return:
    """
    return str(uuid.uuid4())


__all__ = ['ID_TYPE', 'random_id', 'uuid_v1', 'uuid_v4']
