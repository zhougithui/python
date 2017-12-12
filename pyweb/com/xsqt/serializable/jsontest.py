#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""" a test module """

__author__ = 'zmy'


import json


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


if __name__ == '__main__':
    s = Student('Bob', 20, 88)
    print(json.dumps(s, default=student2dict))
    json_str = '{"age": 20, "score": 88, "name": "Bob"}'
    stu = json.loads(json_str, object_hook=dict2student)
    print(stu.name)

