#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""" a test module """

__author__ = 'zmy'

import pika

credentials = pika.PlainCredentials('zh', 'zh')
connection = pika.BlockingConnection(pika.ConnectionParameters("192.168.106.130", 5672, '/', credentials))
channel = connection.channel()
# channel.queue_declare(queue='hello')
#
#
# def callback(ch, method, properties, body):
#     print(" [x] Received %r" % body)
#
#
# channel.basic_consume(callback, 'hello', no_ack=True)

# 创建交换机
channel.exchange_declare(exchange='hello-exchange',
                         exchange_type='direct',
                         passive=False,
                         durable=True,
                         auto_delete=False)
channel.queue_declare(queue='hello-queue')
channel.queue_bind(queue='hello-queue',
                   exchange='hello-exchange',
                   routing_key='zmy')


def msg_consumer(channel, method, header, body):
    channel.basic_ack(delivery_tag=method.delivery_tag)
    if body == 'quit':
        channel.basic_cancel(consumer_tag='hello-consumer')
        channel.stop_consuming()
    else:
        print(body)
    return


channel.basic_consume(msg_consumer,
                      queue='hello-queue',
                      consumer_tag='hello-consumer')

channel.start_consuming()
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()