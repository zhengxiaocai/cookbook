"""
通过下标访问seq难以阅读，可以命名
collection.namedtuple()

TODO
感觉没啥用，先放着吧。
"""
from collections import namedtuple


if __name__ == '__main__':
    my_tuple = ('jonesy@example.com', '2012-10-19')
    Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
    sub = Subscriber(*my_tuple)
    print(sub)
    print(sub.addr)








