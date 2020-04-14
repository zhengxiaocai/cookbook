"""
在序列上保持元素的顺序的同时，删掉重复值
hashable 如果元素是，可以直接搞。
直接用set是不行的，set无序。
带key参数的这个方法比较牛。
"""


# hashable可以的
def dedupe(items):
    seen = []
    for i in items:
        if i not in seen:
            seen.append(i)
    return seen


# 不可hashable，可以用这种更强大的
def dedupe_best(items, key=None):
    seen = []
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.append(val)


if __name__ == '__main__':
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    print(dedupe(a))

    b = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
    print(dedupe(b))

    print(list(dedupe_best(b, key=lambda d: (d['x'], d['y']))))
    print(list(dedupe_best(b, key=lambda d: d['x'])))



