"""
一个数据序列，从规则中提取想要的数据，或者缩短序列
列表表达式，比较占用内存。可以用生成器表达式。
如果条件比较复杂，可以定义一个func，用filter(func, seq)过滤
    注：filter()第一个参数是func
两个序列，元素可以一一对应，一个是bool。可以用 itertools.compress()
"""
from math import sqrt
from itertools import compress


def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    # 最简单的就是列表推导式
    mylist = [1, 4, -5, 10, -7, 2, 3, -1]
    print([i for i in mylist if i > 0])

    # 生成器表达式
    pos = (i for i in mylist if i > 0)
    print(pos)
    print(list(pos))

    # 如果条件比较复杂，先写个过滤函数，然后用filter()过滤
    values = ['1', '2', '-3', '-', '4', 'N/A', '5']
    values_int = filter(is_int, values)
    print(list(values_int))

    # 列表生成器可以在过滤的时候转化数据
    print([sqrt(i) for i in mylist if i > 0])
    # 符合条件 不符合条件，可以分别处理
    print([n if n > 0 else 0 for n in mylist])
    print((n if n < 0 else 0 for n in mylist))

    # 两个一一对应的可迭代对象，另一个是相对应的bool类型
    addresses = [
        '5412 N CLARK',
        '5148 N CLARK',
        '5800 E 58TH',
        '2122 N CLARK',
        '5645 N RAVENSWOOD',
        '1060 W ADDISON',
        '4801 N BROADWAY',
        '1039 W GRANVILLE',
    ]
    counts = [0, 3, 10, 4, 1, 7, 6, 1]
    print([i for i, j in zip(addresses, [x > 5 for x in counts]) if j])
    counts_bool = [i > 5 for i in counts]
    print(list(compress(addresses, counts_bool)))



