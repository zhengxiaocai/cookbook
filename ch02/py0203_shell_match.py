"""
通配符匹配
介于简单匹配和正则匹配之间，小试身手的时候用。
fnmatch.fnmatch()  fnmatch.fnmatchcase()
"""
from fnmatch import fnmatch, fnmatchcase

if __name__ == '__main__':
    print(fnmatch('foo.txt', '*.txt'))
    print(fnmatch('foo.txt', '?oo.txt'))
    print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

    names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
    print([name for name in names if fnmatch(name, 'Dat*.csv')])

    # fnmatch.fnmatch() 大小写根据系统来
    print(fnmatch('foo.txt', '*.TXT'))  # 这个Mac上是False

    # fnmatch.fnmatchcase() 大小写根据统配符匹配
    print(fnmatchcase('foo.txt', '*.TXT'))

    addresses = [
        '5412 N CLARK ST',
        '1060 W ADDISON ST',
        '1039 W GRANVILLE AVE',
        '2122 N CLARK ST',
        '4802 N BROADWAY',
    ]
    print([address for address in addresses if fnmatch(address, '* ST')])
    print([address for address in addresses if fnmatchcase(address, '54[0-9][0-9] *CLARK*')])


