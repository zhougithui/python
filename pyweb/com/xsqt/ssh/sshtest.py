#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""" a test module """

__author__ = 'zmy'


import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.106.132', port=22, username='root', password='123456')

stdin, stdout, stderr = ssh.exec_command('df')
result = stdout.read()

print(result)
ssh.close()


transport = paramiko.Transport(('192.168.106.132', 22))
transport.connect(username='root', password='123456')

ssh = paramiko.SSHClient()
ssh._transport = transport

stdin, stdout, stderr = ssh.exec_command('df')
print(stdout.read())

transport.close()
