# Starlight for RabbitMQ Demo

### Running RabbitMQ.
```
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.10-management
```

### Bind, publish, and consume using RabbitMQ
Bind to 'test-queue' to an 'direct' exchange with 'test-key' routing key.

```
python3 rabbitmq-bind.py direct test-queue test-key
```
  
Start a consumer for this exchange and routing key.

```
python3 rabbitmq-consume.py direct test-queue test-key
```


Start a publisher for this queue and start publishing messages.
```
python3 rabbitmq-publish.py direct test-queue test-key
```

Stop RabbitMQ

### Running S4R on a locally run instance of Apache Pulsar
In order to run Starlight for RabbitMQ locally, you'll need to down load [Apache Pulsar](http://pulsar.apache.org) and the current S4R binaries from the [Starlight for RabbitMQ](https://github.com/datastax/starlight-for-rabbitmq/releases) GitHub repository.

Start Pulsar
```
pulsar standalone
```

Ensure your starlight.conf file contains these values.
```
brokerServiceURL=pulsar://localhost:6650
brokerWebServiceURL=http://localhost:8080
configurationStoreServers=localhost:2181
```

Start S4R as a runnable jar from within the project directory.
```
java -jar starlight-rabbitmq-2.10.0.1-jar-with-dependencies.jar -c starlight.conf
```

Run through the same three python commands again.
```
python3 rabbitmq-bind.py direct test-queue test-key
python3 rabbitmq-publish.py direct test-key
python3 rabbitmq-consume.py test-queue
```

### Using Starlight for RabbitMQ on Astra Streaming
To use S4R on [Astra Streaming](http://astra.datastax.com) you'll need to create a free account and then create a streaming tenant by clicking the `Create Stream` button.  Once this is done, go to your streaming tenant and click the `Connect` tab and then the `RabbitMQ` link.  There you will see connection details needed to interact with S4R on Astra Streaming.

Run the same three python command using the connection details you just retreived.

```
python3 rabbitmq-bind.py direct test-queue test-key <port> <host> <virtual_host> <token>
python3 rabbitmq-publish.py direct test-key <port> <host> <virtual_host> <token>
python3 rabbitmq-consume.py test-queue <port> <host> <virtual_host> <token>
```

