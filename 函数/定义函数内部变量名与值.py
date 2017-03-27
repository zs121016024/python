#!/usr/bin/env python
# coding:utf-8

from collections import namedtuple

User = namedtuple('User', ['name', 'age'])
users = [User('jon', 18), User('paggy', 16), User('tom', 32)]

def get_age(user):
    return user.age

print(sorted(users, key=get_age))


print(sorted(users, key=lambda  x: x.age))

print(list(map(lambda x: x.age, users)))

print(list(filter(lambda x: x.age < 30, users)))