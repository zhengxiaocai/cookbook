"""
解压一个序列(可迭代对象)到指定的多个变量
要求：前边的变量个数跟后边的序列长度一致；数据结构也要一致。
"""

if __name__ == '__main__':
    p = (4, 5)
    x, y = p
    print(x, y)

    # 数据结构一样，就是说的这个
    data = ['ACME', 50, 91.1, (2012, 12, 21)]
    name, shares, prices, date = data
    print('name: {}'.format(name))
    print('date: {}'.format(date))

    name, shares, prices, (year, month, day) = data
    print('year: {}'.format(year))

    # 变量个数不匹配的情况下，会报ValueError
    try:
        x, y, z = p
    except ValueError as e:
        print('ValueError!')

    # 这种赋值，可以用在任何可迭代对象上，比如字符串
    s = 'Hello'
    a, b, c, d, e = s
    print('a: {}'.format(a))

    # 如果只是想要其中一部分，可以用 _ 舍弃
    _, shares, prices, _ = data
    print('prices: {}'.format(prices))
