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
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(heapq.nlargest(3, nums))
    print(heapq.nsmallest(3, nums))

    # 跟sorted() min() 一样，也可以接受一个key参数，用于更复杂的
    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    cheap = heapq.nsmallest(3, portfolio, key=lambda x: x['price'])
    expensive = heapq.nlargest(3, portfolio, key=lambda x: x['price'])
    print(cheap)
    print(expensive)

    # >>TODO: 首先会把list转成heap(堆)，堆的特性就是heap[0]最小
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    heap = list(nums)
    heapq.heapify(heap)
    print(heap)
    print(heapq.heappop(heap))
    print(heap)
