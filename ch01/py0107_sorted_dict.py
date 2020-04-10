"""
你想创建一个字典，并且在迭代和序列化这个字典的时候能控制元素顺序
collections.OrderedDict 内部维护了两个链表，所以比较占用内存
python3.6的时候字典已经有序了？
"""
from collections import OrderedDict
import json


if __name__ == '__main__':
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4
    for key in d:
        print(key, d[key])

    j = json.dumps(d)
    print(j)



