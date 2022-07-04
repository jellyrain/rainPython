import random, math

# 随机返回 (0 ~ 1] 之间的一个数
def zero_to_one_prizes():
    return random.random()

# 随机返回数组中的一个值
def one_value_prizes(arr):
    return random.choice(arr)

# 随机返回数组中的一个值的下标
def one_index_prizes(arr):
    return random.randrange(0, len(arr))

# 从数组中抽取指定数量的值，不重复
def sample_prizes(arr, length):
    return random.sample(arr, length)

# 打乱数组顺序
def upsat_the_order(arr):
    return sample_prizes(arr, len(arr))

# 打乱并按你的要求分组，如果 除不尽 向上取整
def upsat_the_order_and_group(arr, length):
    start = 0
    end = length
    arr = upsat_the_order(arr)
    result = []
    for i in range(1, math.ceil(len(arr) / length) + 1):
        result.append((arr[start : end]))
        start = length * i
        end = length * (i + 1)
    return result

__all__ = ['one_value_prizes', 'one_index_prizes', 'sample_prizes', 'upsat_the_order', 'upsat_the_order_group']