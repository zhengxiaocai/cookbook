"""
怎么实现一个键对应多个值？multidict

d = collections.defaultdict(type)  type in (list, set)
这样定义所有的值的类型就定了。
"""
from collections import defaultdict


if __name__ == '__main__':
    d = {
        'a': [1, 2, 3],
        'b': [4, 5]
    }
    e = {
        'c': {1, 2, 3},
        'd': {4, 5}
    }

    f = defaultdict(list)
    f['a'].append(1)
    f['a'].append(2)
    f['a'].append(3)
    f['b'].append(4)
    f['b'].append(5)
    print(f)

    e = defaultdict(set)
    e['a'].add(1)
    e['a'].add(2)
    e['a'].add(3)
    e['b'].add(4)
    e['b'].add(5)
    print(e)
