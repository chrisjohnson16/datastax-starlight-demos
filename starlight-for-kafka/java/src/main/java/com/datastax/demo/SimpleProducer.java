package com.datastax.demo;

import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;

import java.util.Properties;
import java.util.Scanner;
import java.util.concurrent.ExecutionException;

public class SimpleProducer {
    
    public static final String KAFKA_SERVER_URL = "localhost";
    public static final int KAFKA_SERVER_PORT = 9092;
    public static final String CLIENT_ID = "SampleProducer";
    public static final String TOPIC_NAME = "demo-topic";
    
	public static void main(final String[] args) {

		System.out.println("Publishing direct messages to " + TOPIC_NAME);
		Scanner scanner = new Scanner(System.in);

        Properties properties = new Properties();
        properties.put("bootstrap.servers", KAFKA_SERVER_URL + ":" + KAFKA_SERVER_PORT);
        properties.put("client.id", CLIENT_ID);
        properties.put("key.serializer", "org.apache.kafka.common.serialization.IntegerSerializer");
        properties.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");
    	KafkaProducer<Integer, String> producer = new KafkaProducer<>(properties);
		
        int messageNo = 1;	
        try {
        	while (true) {
				System.out.print("> ");			
				String message = scanner.nextLine();
	
	            	producer.send(new ProducerRecord<>(TOPIC_NAME,
	                        messageNo,
	                        message)).get();
	    			System.out.println(" [x] Sent '" + message + "'");	            	
            } 
		}
        catch (InterruptedException | ExecutionException e) {
            e.printStackTrace();
            producer.close();
        }

	}
}