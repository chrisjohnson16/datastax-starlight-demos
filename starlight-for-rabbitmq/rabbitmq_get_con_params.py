import ssl
import pika

def get_connection_params(args):
    params = ""
    port = "5672"

    if len(args) == 8:
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        context.verify_mode = ssl.CERT_NONE
        context.check_hostname = False
        context.load_default_certs()
        ssl_options = pika.SSLOptions(context)

        params = pika.ConnectionParameters(
            port=args[4],
            host=args[5],
            virtual_host=args[6],
            credentials=pika.PlainCredentials("", args[7]),
            ssl_options=ssl_options)

    else:
        params = pika.ConnectionParameters(port=port)

    return params
