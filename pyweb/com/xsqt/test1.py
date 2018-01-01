#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""" a test module """

__author__ = 'zmy'


# def consumer(name):
#     print("-----> starting eating jiaozi")
#     while True:
#         new_jiaozi = yield
#         print("[%s] is eating jiaozi %s" % (name, new_jiaozi))
#
#
# def producer():
#     r = con.__next__()
#     r = con2.__next__()
#     n = 0
#     while n < 5:
#         n += 1
#         con.send(n)
#         con2.send(n)
#         print("\033[32;1m[producer]\033[0m is making baozi %s" % n)
#
#
# if __name__ == '__main__':
#     con = consumer("c1")
#     con2 = consumer("c2")
#     producer()

# from greenlet import greenlet
#
#
# def test1():
#     print(12)
#     gr2.switch()
#     print(34)
#     gr2.switch()
#
#
# def test2():
#     print(56)
#     gr1.switch()
#     print(78)
#
#
# gr1 = greenlet(test1)
# gr2 = greenlet(test2)
# gr1.switch()


# import gevent
#
#
# def func1():
#     print('\033[31;1m李闯在跟海涛搞...\033[0m')
#     gevent.sleep(2)
#     print('\033[31;1m李闯又回去跟继续跟海涛搞...\033[0m')
#
#
# def func2():
#     print('\033[32;1m李闯切换到了跟海龙搞...\033[0m')
#     gevent.sleep(1)
#     print('\033[32;1m李闯搞完了海涛，回来继续跟海龙搞...\033[0m')
#
#
# gevent.joinall([
#     gevent.spawn(func1),
#     gevent.spawn(func2),
#     # gevent.spawn(func3),
# ])


# import gevent
#
#
# def task(pid):
#     """
#     Some non-deterministic task
#     """
#     gevent.sleep(0.5)
#     print('Task %s done' % pid)
#
#
# def synchronous():
#     for i in range(1, 10):
#         task(i)
#
#
# def asynchronous():
#     threads = [gevent.spawn(task, i) for i in range(10)]
#     gevent.joinall(threads)
#
#
# print('Synchronous:')
# synchronous()
#
# print('Asynchronous:')
# asynchronous()

#
# from gevent import monkey
# import gevent
# from urllib.request import urlopen
#
# monkey.patch_all()
#
#
# def f(url):
#     print('GET: %s' % url)
#     resp = urlopen(url)
#     data = resp.read()
#     print('%d bytes received from %s.' % (len(data), url))
#
#
# gevent.joinall([
#     gevent.spawn(f, 'https://www.python.org/'),
#     gevent.spawn(f, 'https://www.yahoo.com/'),
#     gevent.spawn(f, 'https://github.com/'),
# ])

