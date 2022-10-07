#!/usr/bin/env python
import sys
import ssl
import pika
from rabbitmq_get_con_params import *

if len(sys.argv) not in [4, 5] or (len(sys.argv) == 5 and sys.argv[4] != "--astra") :
    print("usage: python rabbitmq-bind.py <exchange_name> <queue_name> <routing_key> [--astra]")
    sys.exit(-1)

exchange = sys.argv[1]
queue = sys.argv[2]
routing_key = sys.argv[3]

try:
    print ("Binding exchange: exchange=" + exchange + " queue=" + queue + " routing_key=" + routing_key)

    connection = pika.BlockingConnection(get_connection_params(sys.argv))
    channel = connection.channel()

    channel.exchange_declare(exchange=exchange)
    print("exchange declared")

    channel.queue_declare(queue=queue)
    print("queue declared")

    channel.queue_bind(exchange=exchange, queue=queue, routing_key=routing_key)
    print("queue bound")

finally:
    connection.close()
