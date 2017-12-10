#! /usr/bin/evn python
# -*- coding: utf-8 -*-


def is_odd(n):
    return n % 2 == 1


def not_empty(s):
    return s and s.strip()


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


for n in primes():
    if n < 100:
        print(n)
    else:
        break


def abc(obj):
    return obj[1]


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(L, key=abc))


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def build(x, y):
    return lambda: x + y


print(build(1, 2)())


X = list(filter(lambda b: b % 2 == 1, range(1, 20)))


print(X)


