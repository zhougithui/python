#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""" a test module """

__author__ = 'zmy'
from io import StringIO
from io import BytesIO

try:
    f = open('d:/dev-test', 'r')
    context = f.read()
    print(context)
finally:
    if f:
        f.close()


with open('d:/dev-test', 'r') as f:
    print(f.read())

with open('d:/dev-test', 'r') as f:
    for line in f.readlines():
        print(line.strip())

with open('d:/dev-test', 'r', encoding='gbk', errors='ignore') as f:
    for line in f.readlines():
        print(line.strip())

with open('d:/1.txt', 'w', encoding='gbk') as f:
    f.write('abc')

f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

