"""
在迭代操作或者其他操作的时候，怎样保留有限的几个记录？
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
        for line, prevlines in search(f, ',', 5):
            for pline in prevlines:
                print(pline, end='')
            # print(line, end='')
            print('-' * 20)

    q = deque(maxlen=3)
    q.append(1)
    q.append(2)
    q.append(3)
    print(q)
    q.append(4)
    print(q)
    q.append(5)
    print(q)

    # 如果不设置maxlen，就会得到一个无限长度的len
    # 可以在队列的两端执行添加和弹出操作
    d = deque()
    d.append(1)
    d.append(2)
    d.append(3)
    print(d)
    d.appendleft(4)
    print(d)
    d.popleft()
    print(d)
    d.append(5)
    print(d)
    d.pop()
    print(d)

    # 在队列的两端增删元素的时间复杂度为O(1),在列表为O(n)


