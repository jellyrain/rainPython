import math
import random


def zero_to_one_prizes():
    """ 随机返回 (0 ~ 1] 之间的一个数 """
    return random.random()


def random_range_prizes(start, end, is_float=False):
    """ 随机返回 指定范围的值 """
    return random.uniform(start, end) if is_float else random.randint(start, end)


def one_value_prizes(arr):
    """ 随机返回数组中的一个值 """
    return random.choice(arr)


def one_index_prizes(arr):
    """ 随机返回数组中的一个值的下标 """
    return random.randrange(0, len(arr))


def sample_prizes(arr, length):
    """ 从数组中抽取指定数量的值，不重复 """
    return random.sample(arr, length)


def upset_the_order(arr):
    """ 打乱数组顺序 """
    return sample_prizes(arr, len(arr))


def upset_the_order_and_group(arr, length):
    """ 打乱并按你的要求分组，如果 除不尽 向上取整 """
    start = 0
    end = length
    arr = upset_the_order(arr)
    result = []
    for i in range(1, math.ceil(len(arr) / length) + 1):
        result.append((arr[start: end]))
        start = length * i
        end = length * (i + 1)
    return result


__all__ = ['one_value_prizes', 'one_index_prizes', 'sample_prizes', 'upset_the_order', 'upset_the_order_and_group']
