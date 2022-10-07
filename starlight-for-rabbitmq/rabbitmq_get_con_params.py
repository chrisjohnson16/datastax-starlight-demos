import ssl
import pika
from rabbitmq import *

def get_connection_params(args):
    params = ""

    if len(args) == 5:
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        context.verify_mode = ssl.CERT_NONE
        context.check_hostname = False
        context.load_default_certs()
        ssl_options = pika.SSLOptions(context)

        params = pika.ConnectionParameters(
            port=port,
            host=host,
            virtual_host=virtual_host,
            credentials=pika.PlainCredentials("", password),
            ssl_options=ssl_options)

    else:
        params = pika.ConnectionParameters(port=5672)

    return params
