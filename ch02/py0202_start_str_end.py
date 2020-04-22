"""
通过指定的文本模式去匹配字符串的开头或者结尾。
简单模式：
    str.startswith()    str.endswith()
多个选择符：  参数必须是个tuple
    str.startswith(tuple())     str.endswith(tuple())
"""
import os
import re


def read_data(url_name):
    if url_name.startswith(('http:', 'https:', 'ftp:')):
        print('url')
    else:
        print('not url')


if __name__ == '__main__':
    filename = 'spam.txt'
    print(filename.endswith('.txt'))
    print(filename.startswith('file:'))

    url = 'http://www.python.org'
    print(url.startswith('http:'))

    # 检查多种匹配的可能，将所有的匹配项放在一个元组中
    filenames = os.listdir('../ch01')
    # for file in sorted(filenames):
    #     print(file)
    print([file for file in filenames if file.startswith('py0103')])
    print([file for file in filenames if file.startswith(('py0103', 'py0104'))])

    print(any(file.startswith('py') for file in filenames))
    print(all(file.endswith(('.py', '.txt')) for file in filenames))

    # 如果有多个需要匹配，入参必须是tuple，如果正好有个list set，也需要用tuple转一下
    choices = ['http:', 'https:']
    try:
        url.startswith(choices)
    except TypeError:
        print(TypeError)

    print(url.startswith(tuple(choices)))

    # 类似的功能可以用切片 正则完成，不优雅
    print(filename[-4:] == '.txt')

    print(re.match(r'https:|http:|ftp:', url))
