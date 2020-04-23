"""
把多个字典或映射，从逻辑上合并为一个单一的映射执行某些操作。
"""
from collections import ChainMap


if __name__ == '__main__':
    a = {'x': 1, 'z': 3}
    b = {'y': 2, 'z': 4}
    c = ChainMap(a, b)
    print(c['x'])
    print(c['y'])
    print(c['z'])

    # ChainMap() 逻辑上变为一个字典。如果重复，取第一个的。
    print(len(c))
    print(list(c.keys()))
    print(list(c.values()))

    # 删除 修改也都是影响第一个字典。
    c['z'] = 10
    c['w'] = 40
    print(c)

    try:
        del c['y']
    except KeyError:
        print('a 没有键 y')

    values = ChainMap()
    values['x'] = 1
    values = values.new_child()
    values['x'] = 2
    values = values.new_child()
    values['x'] = 3

    print(values)

    values = values.parents
    print(values)

    values = values.parents
    print(values)

    # 也可以用 dict.update(dict) 方法，破坏了现有的数据结构。
    merged = dict(b)
    merged.update(a)
    print(merged)
    # 破坏了之前的数据结构，新的改变也不会更新到新建的数据上。
    a['x'] = 13
    print(merged['x'])

    i = {'x': 1, 'z': 3}
    j = {'y': 2, 'z': 4}
    merg = ChainMap(i, j)
    print(merg['x'])
    i['x'] = 42
    print(merg['x'])


