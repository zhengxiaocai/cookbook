"""
怎样找出一个序列中出现次数最多的元素。
sorted()默认是升序
用collections.Counter计数，得到的是一个字典。
可以后续更新计数： +=  .update(list)
结果集之间可以进行加减数学运算。
"""
from collections import Counter


if __name__ == '__main__':
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'
    ]

    # 通常做法
    items_count = {}
    for word in words:
        if word not in items_count:
            items_count[word] = 0
        items_count[word] += 1
    print(items_count)
    # 出现最多的三个，需要排序。
    sorted_items_count = sorted([i for i in items_count.items()], key=lambda x: x[1], reverse=True)
    print(sorted_items_count[:3])

    # 新方法 collections.Counter。生成的对象本身就是一个字典。
    words_counter = Counter(words)
    print(words_counter.most_common(3))

    # 手动更新数据。字典赋值，自增；obj.update[list]，把list的加一个计数。
    print(words_counter['eyes'])
    words_counter['eyes'] += 1
    print(words_counter['eyes'])
    words_counter.update(['eyes'])
    print(words_counter['eyes'])

    # 可以加减数学运算。
    more_words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't"]
    another_counter = Counter(more_words)
    print(words_counter + another_counter)
    print(words_counter - another_counter)
