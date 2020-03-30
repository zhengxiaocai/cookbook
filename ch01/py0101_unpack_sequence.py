"""
解压一个序列(可迭代对象)到指定的多个变量
要求：前边的变量个数跟后边的序列长度一致；数据结构也要一致。
"""

if __name__ == '__main__':
    p = (5, 6)
    x, y = p
    print(x, y)

    data = ['ACME', 50, 91.1, (2012, 12, 21)]
    name, shares, price, date = data
    print(name, shares, price, date)

    name, shares, price, (year, mon, day) = data
    print(year, mon, day)

    # 如果变量个数跟序列长度不匹配，就会引发异常。 ValueError
    # name, shares = data

    # 只要是可迭代对象就可以
    zero, one = range(2)
    print(type(range(2)))
    print(zero, one)

    # 解压过程中想丢弃某些，可以用 _ ，接受 然后不用
    name, _, _, date = data
    print(_)
