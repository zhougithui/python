#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""" a test module """

__author__ = 'zmy'


import os

print(os.name)
# print(os.uname())

print(os.environ)

print(os.environ.get('path'))

print(os.path.abspath('.'))

print(os.path.join('d:/', 'txt'))

os.mkdir('d:/txt')
os.rmdir("d:/txt")


path = os.path.split('d:/txt/1.txt')
path = os.path.splitext('d:/txt/1.txt')
print(path)


f = [x for x in os.listdir('d:/') if os.path.isdir('d:/' + x)]
print(f)
