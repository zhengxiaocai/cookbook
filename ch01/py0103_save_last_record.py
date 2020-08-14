"""
在迭代操作或者其他操作的时候，怎样保留有限的几个记录？
>>TODO: 在deque()两端操作，时间复杂度都是O(1),列表是O(n)
"""
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    with open('py0103.txt', 'r') as f:
        for line, previous_lines in search(f, ','):
            for pline in previous_lines:
                print(pline, end='')
            print('=' * 20)

    # 大小定死的一个容器，先进先出
    q = deque(maxlen=3)
    q.append(1)
    q.append(2)
    q.append(3)
    print(q)
    q.append(4)
    print(q)
    q.append(5)
    print(q)
    q.appendleft(6)
    print(q)

    # 不设定最大宽度，就是一个无限的
    p = deque()
    p.append(1)
    p.append(2)
    p.append(3)

    # >>TODO: 左边操作 appendleft(a)  popleft()
    p.appendleft(4)
    p.popleft()
    print(p)
