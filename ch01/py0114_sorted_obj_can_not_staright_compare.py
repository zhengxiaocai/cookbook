"""
你想排序类型相同的对象，但是他们不支持原生的比较操作。
operator.attrgetter()
同时支持sorted() min() max()
"""
from operator import attrgetter


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return f'User({self.user_id})'


def sorted_not_compare(users):
    return sorted(users, key=lambda x: x.user_id)


def sorted_by_attrgetter(users):
    return sorted(users, key=attrgetter('user_id'))


if __name__ == '__main__':
    user = [User(23), User(3), User(99)]
    print(sorted_not_compare(user))
    print(sorted_by_attrgetter(user))


