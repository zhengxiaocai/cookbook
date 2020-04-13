"""
在两个字典之间，寻找共同点：共同的键，共同的值，共同的键值对。
获取键 值 键值对 然后集合计算。& 交集；- 差急；| 并集
！！！值是不支持的，需要转成set()才行。
"""


if __name__ == '__main__':
    a = {
        'x': 1,
        'y': 2,
        'z': 3}
    b = {
        'w': 10,
        'x': 11,
        'y': 2}
    print(a.keys() & b.keys())
    print(a.keys() - b.keys())
    print(a.items() & b.items())
    print(a.keys() | b.keys())
    print(type(a.keys()))

    # 生成式中过滤条件。
    c = {key: a[key] for key in a.keys() - {'z', 'w'}}
    print(c)

    # dict.values() 没有这么多操作。
    # print(a.values() & b.values())
