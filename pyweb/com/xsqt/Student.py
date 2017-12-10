#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""" a test module """

__author__ = 'zmy'


class Student(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def tostring(self):
        print('student name=%s, age= %s' % (self.__name, self.__age))


if __name__ == '__main__':
    zmy = Student('zmy', 18)
    zmy.tostring()


