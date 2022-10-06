#!/usr/bin/env python
import sys

import ssl
import pika
from rabbitmq_get_con_params import *

if len(sys.argv) not in [4, 8]:
    print("usage: python rabbitmq-bind.py <exchange_name> <queue_name> <routing_key> [<port> <host> <virtual_host> <toke>]")
    sys.exit(-1)

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
