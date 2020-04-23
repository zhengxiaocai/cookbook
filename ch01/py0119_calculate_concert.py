"""
需要在seq执行聚集函数（sun() max() min()），还需要转化数据
[]还是不能随便加，应为()是生成器。
如果用在聚集函数时，sum() min() max()不要加[]
"""
import os


if __name__ == '__main__':
    # 计算平方和
    nums = [1, 2, 3, 4, 5]
    print(sum(x * x for x in nums))

    files = os.listdir('/Users/hanxing/PycharmProjects/cookbook3/ch01')
    # for file in files:
    #     print('file', file)
    if any(name.endswith('.py') for name in files):
        print('There be python!')
    else:
        print('Sorry, no Python!')

    s = ('ACME', 50, 123.45)
    print(','.join(str(x) for x in s))

    portfolio = [
        {'name': 'GOOG', 'shares': 50},
        {'name': 'YHOO', 'shares': 75},
        {'name': 'AOL', 'shares': 20},
        {'name': 'SCOX', 'shares': 65}
    ]
    min_shares = min([item['shares'] for item in portfolio])
    print(min_shares)

    # 以下两个等效，直接用生成器表达式，更加优雅 高效 节省内存
    s = sum((x*x for x in nums))
    s = sum([x*x for x in nums])
    s = sum(x*x for x in nums)

    min_shares_1 = min(item['shares'] for item in portfolio)
    min_shares_2 = min(portfolio, key=lambda x: x['shares'])
    print(min_shares_1)
    print(min_shares_2)



