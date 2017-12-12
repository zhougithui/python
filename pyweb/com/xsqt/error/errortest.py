#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""" a test module """

__author__ = 'zmy'

import logging

try:
    print('try ....')
    raise ValueError('error value 0')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
    logging.exception(e)
else:
    print('no error')
finally:
    print('finally..')

print('end')
