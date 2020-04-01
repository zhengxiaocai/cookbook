"""
怎样实现一个按优先级排序的队列?并且在这个队列上面每次 pop
操作总是返回 优先级最高的那个元素

heapq.heappush(heap, item)
把item推到heap中，保持第一个为最小。
"""
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
        # print('-'*20, self._queue)

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


if __name__ == '__main__':
    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 1)
    q.push(Item('spam'), 4)
    q.push(Item('grok'), 5)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())



