"""
怎样从一个集合中获得最大或者最小的 N 个元素列表?
heapq.nsmallest(n, seq)
首先使用堆排序，然后放到一个列表中。

如果：n=1      max() min()
如果：1< <<n   heapq.nsmallest(n, seq)     heapq.nlargest(n, seq)
如果：1<< <n   sort(seq)[:N]
"""
import heapq


if __name__ == '__main__':
    # 简单示例
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2, -3]
    print(heapq.nlargest(3, nums))
    print(heapq.nsmallest(3, nums))

    # 使用于复杂模型，使用lambda
    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    print(heapq.nlargest(3, portfolio, lambda x: x['price']))
    print(heapq.nsmallest(3, portfolio, lambda x: x['shares']))

    # 堆排序heap[0]永远是最小的。
    # nsmallest内部实现，首先放入list，然后heapq.heapify(list(seq))
    # 第一个元素用  heapq.heapify(heap)，剩下的用heapq.heappop(heap)实现。
    heap = list(nums)
    heapq.heapify(heap)
    print(heap)

    print(heapq.heappop(heap))
    print(heapq.heappop(heap))
    print(heapq.heappop(heap))



