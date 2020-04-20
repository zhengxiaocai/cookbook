"""
构建一个字典，是另一个字典的子集

"""


if __name__ == '__main__':
    # 通过字典推导式
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }
    prices_over_200 = {key: value for key, value in prices.items() if value > 200}
    print(prices_over_200)
    tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
    prices_name = {key: value for key, value in prices.items() if key in tech_names}
    print(prices_name)

    # 通过dict()转化元组序列也是可以的，不过慢2倍
    p1 = dict((key, value) for key, value in prices.items() if value > 200)
    print(p1)

    # 也可以生成的时候，用dict[key]的形式，这样慢1.6倍
    p2 = {key: prices[key] for key, value in prices.items() if key in tech_names}
    print(p2)

