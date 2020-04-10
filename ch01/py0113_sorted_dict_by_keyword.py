"""
你有一个字典列表，你想根据某几个字典字段来排序这个列表
相较于lambda方式，该种性能更好。
    lambda 也是可以传入多个key
放到sorted() max() min()里边都是可以的。
"""
from operator import itemgetter


if __name__ == '__main__':
    rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ]
    rows_by_fname = sorted(rows, key=itemgetter('fname'))
    rows_by_fname_lambda = sorted(rows, key=lambda x: x['fname'])
    print(rows_by_fname)
    print(rows_by_fname_lambda)

    rows_by_uid = sorted(rows, key=itemgetter('uid'))
    rows_by_uid_lambda = sorted(rows, key=lambda x: x['uid'])
    print(rows_by_uid)
    print(rows_by_uid_lambda)

    rows_by_lname = sorted(rows, key=itemgetter('lname', 'fname'))
    rows_by_lname_lambda = sorted(rows, key=lambda x: (x['lname'], x['fname']))
    print(rows_by_lname)
    print(rows_by_lname_lambda)

    max_by_uid = max(rows, key=itemgetter('uid'))
    print(max_by_uid)



