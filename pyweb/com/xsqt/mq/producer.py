#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""" a test module """

__author__ = 'zmy'

import pika


credentials = pika.PlainCredentials('zh', 'zh')
connection = pika.BlockingConnection(pika.ConnectionParameters("192.168.106.132", 5672, '/', credentials))
channel = connection.channel()

# 默认虚拟主机、默认交换机
# channel.queue_declare(queue='hello')
# channel.basic_publish(exchange='', routing_key='hello', body='Hello world')

# 创建交换机
channel.exchange_declare(exchange='hello-exchange',
                         exchange_type='direct',
                         passive=False,
                         durable=True,
                         auto_delete=False)
while True:
    msg = input("code msg.....")
    msg_props = pika.BasicProperties()
    msg_props.content_type = "text/plain"
    channel.basic_publish(body=msg,
                          exchange='hello-exchange',
                          properties=msg_props,
                          routing_key='zmy')

# print("[x] Sent 'Hello World!'")
connection.close()
