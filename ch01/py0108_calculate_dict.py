"""
怎样在数据字典中执行一些计算操作(比如求最小值、最大值、排序等等)?
通过zip反转，然后用min() max() sorted()
这个过时了，极客时间大佬解法：
min(dict.items(), key=lambda x: x[1])
"""


if __name__ == '__main__':
    # 股票名和价格
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }

    # 价格最高和最低的股票名和价格
    min_p = min(zip(prices.values(), prices.keys()))
    print(min_p)
    max_p = max(zip(prices.values(), prices.keys()))
    print(max_p)

    # 升序排列，sorted()默认的就是升序。
    sorted_p = sorted(zip(prices.values(), prices.keys()))
    print(sorted_p)

    # ！！！zip()创建的只能访问一次，再次访问就报错了。
    prices_and_name = zip(prices.values(), prices.keys())
    print(min(prices_and_name))
    # print(max(prices_and_name))

    # 直接运算的时候，运算的是key
    print(min(prices))

    # 直接运算values，但是，不知道属于哪个key
    print(min(prices.values()))

    # 可以用lambda表达式
    print(min(prices, key=lambda x: prices[x]))

    # 极客时间大佬的解法
    print(min(prices.items(), key=lambda x: x[1]))
    sorted_price = dict(sorted(prices.items(), key=lambda x: x[1]))
    print(sorted_price)







