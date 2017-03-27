#!/usr/bin/env python
# coding:utf-8

def outer():
    def inner():
        print('inner')
    print('outer')
    inner()
print(outer())