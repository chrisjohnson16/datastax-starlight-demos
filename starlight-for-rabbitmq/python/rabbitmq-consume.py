#!/usr/bin/env python
import sys

import ssl
import pika
from rabbitmq_get_con_params import *

if len(sys.argv) not in [4, 5] or (len(sys.argv) == 5 and sys.argv[4] != "--astra") :
    print("usage: python rabbitmq-consume.py <exchange_name> <queue_name> <routing_key> [--astra]")
    sys.exit(-1)

exchange = sys.argv[1]
queue = sys.argv[2]
routing_key = sys.argv[3]

try:
    print ("Waiting for messages: exchange=" + exchange + " queue=" + queue + " routing_key=" + routing_key)

    def on_message(channel, method_frame, header_frame, body):
        print("Message: ", body.decode())

    connection = pika.BlockingConnection(get_connection_params(sys.argv))
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    channel.basic_consume(queue, on_message, auto_ack=True)
    channel.start_consuming()

except KeyboardInterrupt:
    channel.stop_consuming()
    connection.close()
