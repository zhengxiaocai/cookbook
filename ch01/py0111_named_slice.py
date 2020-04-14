"""
代码里出现了一堆硬编码下标，起个别名更清楚。
var = slice(start, end, step=None)
既可以取值，也可以赋值改变。
"""


if __name__ == '__main__':
    record = '....................100 .......513.25 ..........'
    cost = int(record[20:23]) * int(float(record[31:37]))
    print(cost)

    # 可以直接赋值给变量，通过变量执行后续操作。
    SHARES = slice(20, 23)
    PRICES = slice(31, 37)
    cost = int(record[SHARES]) * float(record[PRICES])
    print(cost)

    items = [0, 1, 2, 3, 4, 5, 6]
    a = slice(2, 4)
    print(items[2:4], items[a])
    # 通过切片别名赋值。
    items[a] = [10, 11]
    print(items)
    # 通过切片别名删除。
    del items[a]
    print(items)

    # 通过var.start var.stop var.step 属性，获取具体的值。
    print(a.start, a.stop, a.step)

    # 通过 var.indices(len) 获得一个满足边界的三元组
    # 感觉没啥用呀。
    s = 'HelloWorld'
    print(a.indices(len(s)))
    for i in range(*a.indices(len(s))):
        print(s[i])


