"""
可迭代对象超过变量个数，从可迭代对象中解压n个元素；序列是有某种规律的。用 * 来分类。
得到的永远是个列表。
"""


def drop_first_last(grades):
    """
    去掉一个最高分，去掉一个最低分，算平均
    :param grades: 按顺序排列的成绩
    :return: 平均成绩
    """
    _, *avg, _ = grades
    return sum(avg) / len(avg)


def do_foo(a, b):
    print('foo', a, b)


def do_bar(a):
    print('bar', a)


if __name__ == '__main__':
    # 有用户记录，前边两个是姓名 邮箱，后边跟着n个电话
    record = ['Dave', 'dave@example.com', '733-555-1212', '847-555-1212']
    name, email, *mobile = record
    print(name, email, mobile)

    # * 当然也可以放到前边的
    # 例：当前有八个月的数据，相比较下当前月跟前七个月的平均数
    *trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
    trailing_avg = sum(trailing) / len(trailing)
    print(trailing_avg, current)

    # 对于可变长的元组序列特别有用
    records = [
        ('foo', 1, 2),
        ('bar', 'hello'),
        ('foo', 3, 4)
    ]

    for tag, *args in records:
        if tag == 'foo':
            do_foo(*args)
        elif tag == 'bar':
            do_bar(*args)

    # 对于切割字符串也是很有用的
    line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
    name, *fields, homedir, sh = line.split(':')
    print(name, homedir, sh)

    # 想丢弃某些时，用  *_
    # 下面这个例子，只想保留name, year
    record = ('ACME', 50, 123.45, (12, 18, 2012))
    name, *_, (*_, year) = record
    print(name, year)

