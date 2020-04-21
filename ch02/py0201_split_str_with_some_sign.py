"""
将字符串分割为多段，分隔符不固定
"""
import re
from itertools import zip_longest

if __name__ == '__main__':
    line = 'asdf  fjdk;  afed,  fjek,asdf, foo'
    split_line = re.split(r'[;,\s]\s*', line)
    print(split_line)

    # 如果存在捕获()，则捕获的也可以返回。
    split_line_get = re.split(r'(;|,|\s)\s*', line)
    print(split_line_get)

    # 可以保留分隔符，用于后边构建新的字符串
    values = split_line_get[::2]
    delimiters = split_line_get[1::2]
    print(values)
    print(delimiters)
    new_s = ''.join('{}{}'.format(v, d if d else '') for v, d in zip_longest(values, delimiters))
    print(new_s)

    # 不想保留分割符号，仍然要用括号，要确保分组是非捕获的。(?:...)
    print(re.split(r'(?:,|;|\s)\s*', line))


