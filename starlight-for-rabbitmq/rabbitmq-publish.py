#!/usr/bin/env python
import sys

import ssl
import pika
from rabbitmq_get_con_params import *

if len(sys.argv) not in [4, 8]:
    print("usage: python rabbitmq-publish.py <exchange_name> <queue_name> <routing_key> [<port> <host> <virtual_host> <toke>]")
    sys.exit(-1)

exchange = sys.argv[1]
queue = sys.argv[2]
routing_key = sys.argv[3]

try:
    print ("Publishing messages: exchange=" + exchange + " queue=" + queue + " routing_key=" + routing_key)

    connection = pika.BlockingConnection(get_connection_params(sys.argv))
    channel = connection.channel()
    channel.exchange_declare(exchange=exchange)
    channel.confirm_delivery()

    while True:
        msg = input("> ")
        channel.basic_publish(exchange=exchange,
                              routing_key=routing_key,
                              body=msg.encode('utf-8'))
        print("Message: " + msg)

except KeyboardInterrupt:
    connection.close()
