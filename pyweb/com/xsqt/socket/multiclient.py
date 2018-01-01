#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""" a test module """

__author__ = 'zmy'


import socket
import threading


def sock_conn():
    client = socket.socket()
    client.connect(("localhost", 8001))
    count = 0
    while True:
        # msg = input(">>:").strip()
        # if len(msg) == 0:continue
        client.send(("hello %s" % count).encode("utf-8"))

        data = client.recv(1024)

        # 结果
        print("[%s]recv from server:" % threading.get_ident(), data.decode())
        count += 1
    client.close()


for i in range(100):
    t = threading.Thread(target=sock_conn)
    t.start()

