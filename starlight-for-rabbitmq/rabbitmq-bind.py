#!/usr/bin/env python
import sys

import ssl
import pika
from rabbitmq_get_con_params import *

if len(sys.argv) not in [4, 8]:
    print("usage: python rabbitmq-bind.py <exchange_name> <queue_name> <routing_key> [<port> <host> <virtual_host> <toke>]")
    sys.exit(-1)

#virtual_host = "astra-demo/rabbitmq"
#token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NjUwNjI2MzIsImlzcyI6ImRhdGFzdGF4Iiwic3ViIjoiY2xpZW50O2Y2OWU2OWEyLTM5ODEtNDRhMS04MDQ4LTQ1YjU0MmQwOTA2NDtZWE4wY21FdFpHVnRidz09OzE3MjBjMDdlZGIiLCJ0b2tlbmlkIjoiMTcyMGMwN2VkYiJ9.Ba0FAYh2yrbY3o0XeYdMhAHCV_zVqy3rdna5wIv0Ku3ON8pidQMTdZCBoNl5-Z4Ihvu8E_UnH91x3663pSU1doDBk9IPS7iLO2oGNlOsTtEkK5kyb2FTwB8N6QtL5YK1ZPhsbhoPLYZmu4pgZmOToWgML1JNlLM4G94lVOhNnWE12U_A2IrQw4C3BvZibJQn1CItGi6cfyLW3oQmB1ILBtn5ojp7kOfrIVDwKsCrOasPTJmE9o6AHFhOwaWmLLpPwfukhBug4P2FLxATjXbxn7EdoeO0eFQmnuxcBhyEWkhNCDqYK7BmbvNW-yGxz95KLytuAZiYIz0FQ5VuaTfomQ"


exchange = sys.argv[1]
queue = sys.argv[2]
routing_key = sys.argv[3]

connection = pika.BlockingConnection(get_connection_params(sys.argv))

channel = connection.channel()

try:
    channel.exchange_declare(exchange=exchange)
    print("exchange declared")
    channel.queue_declare(queue=queue)
    print("queue declared")
    channel.queue_bind(exchange=exchange, queue=queue, routing_key=routing_key)
    print("queue bound")
finally:
    connection.close()
