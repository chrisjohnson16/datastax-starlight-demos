package com.datastax.demo;

import java.util.Scanner;

import org.springframework.amqp.core.AmqpTemplate;
import org.springframework.amqp.core.Queue;

import lombok.Setter;

@Setter
public class DirectSender implements Sender {

    private Queue queue;

    private AmqpTemplate template;
    
	public void send() {

		System.out.println("Publishing direct messages to " + queue.getName());
		Scanner scanner = new Scanner(System.in);

		try {
			while (true) {
				System.out.print("> ");			
				String message = scanner.nextLine();
	
				template.convertAndSend(queue.getName(), 
										message);
	
				System.out.println(" [x] Sent '" + message + "'");
			}
		}
		catch(Exception e) {
			scanner.close();
		}

	}
}
