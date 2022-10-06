import ssl
import pika

virtual_host = "astra-demo/rabbitmq"
token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NjUwNjI2MzIsImlzcyI6ImRhdGFzdGF4Iiwic3ViIjoiY2xpZW50O2Y2OWU2OWEyLTM5ODEtNDRhMS04MDQ4LTQ1YjU0MmQwOTA2NDtZWE4wY21FdFpHVnRidz09OzE3MjBjMDdlZGIiLCJ0b2tlbmlkIjoiMTcyMGMwN2VkYiJ9.Ba0FAYh2yrbY3o0XeYdMhAHCV_zVqy3rdna5wIv0Ku3ON8pidQMTdZCBoNl5-Z4Ihvu8E_UnH91x3663pSU1doDBk9IPS7iLO2oGNlOsTtEkK5kyb2FTwB8N6QtL5YK1ZPhsbhoPLYZmu4pgZmOToWgML1JNlLM4G94lVOhNnWE12U_A2IrQw4C3BvZibJQn1CItGi6cfyLW3oQmB1ILBtn5ojp7kOfrIVDwKsCrOasPTJmE9o6AHFhOwaWmLLpPwfukhBug4P2FLxATjXbxn7EdoeO0eFQmnuxcBhyEWkhNCDqYK7BmbvNW-yGxz95KLytuAZiYIz0FQ5VuaTfomQ"

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.verify_mode = ssl.CERT_NONE
context.check_hostname = False
context.load_default_certs()
ssl_options = pika.SSLOptions(context)

connection = pika.BlockingConnection(pika.ConnectionParameters(
    virtual_host=virtual_host,
    host="rabbitmq-gcp-uscentral1.streaming.datastax.com",
    ssl_options=ssl_options,
    port=5671,
    credentials=pika.PlainCredentials("", token)))
print("connection success")

channel = connection.channel()
print("started a channel")

channel.queue_declare(queue='queuename')

for x in range(10):
    channel.basic_publish(exchange='',
                      routing_key='routingkey',
                      body='message body goes here')
    print(" sent one")

connection.close()
