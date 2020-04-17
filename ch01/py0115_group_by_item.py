"""
你有个字典或者实例的序列，想要根据某个特定的字段进行分组。
先排序 operator.itemgetter()，再分组 itertools.groupby()

"""
from itertools import groupby
from operator import itemgetter
from collections import defaultdict


if __name__ == '__main__':
    rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
    ]
    sorted_rows = sorted(rows, key=itemgetter('date'))
    print(sorted_rows)

    # 调用itertools.groupby()
    for date, items in groupby(sorted_rows, key=itemgetter('date')):
        print(date)
        for item in items:
            print('\t', item)

    # 如果是仅仅想结构化到一个大的数据结构去，可以使用字典。
    rows_by_date = defaultdict(list)
    for row in rows:
        rows_by_date[row['date']].append(row)
    print(rows_by_date)

