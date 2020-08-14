"""
可迭代对象超过变量个数，从可迭代对象中解压n个元素；序列是有某种规律的。用 * 来分类。
*后边的变量，解压得到的永远是个列表。
"""
import math


def drop_first_last(grades):
    first, *middle, last = grades
    return sum(middle) / len(middle)


def do_foo(a, b):
    print('foo', a, b)


def do_bar(a):
    print('bar', a)


if __name__ == '__main__':
    # 只知道前边是name，email，后边有不定个数的phone
    record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
    name, email, *phone = record
    print('name: {}'.format(name))
    print('phone: {}'.format(phone))

    # 可变元组序列
    records = [
        ('foo', 1, 2),
        ('bar', 'hello'),
        ('foo', 3, 4),
    ]
    for tag, *args in record:
        if tag == 'bar':
            do_bar(*args)
        elif tag == 'foo':
            do_foo(*args)

    # 字符串分割
    line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
    username, *fields, homedir, sh = line.split(':')
    print('homedir: {}'.format(homedir))

    # 如果要丢弃一部分，也是下划线
    record = ('ACME', 50, 123.45, (12, 18, 2012))
    name, *_, (*_, year) = record
