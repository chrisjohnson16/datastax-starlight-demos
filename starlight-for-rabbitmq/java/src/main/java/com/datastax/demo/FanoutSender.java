package com.datastax.demo;

import java.util.Scanner;

import org.springframework.amqp.core.AmqpTemplate;
import org.springframework.amqp.core.FanoutExchange;

import lombok.Setter;

@Setter
public class FanoutSender implements Sender {

    private AmqpTemplate template;
        
    private FanoutExchange exchange;
    
	public void send() {

		System.out.println("Publishing fanout messages to exchange " + exchange.getName());
		Scanner scanner = new Scanner(System.in);
		
		try {
			while (true) {
				System.out.print("> ");			
				String message = scanner.nextLine();
	
				template.convertAndSend(exchange.getName(), 
										"", 
										message);
	
				System.out.println(" [x] Sent '" + message + "'");
			}
		}
		catch(Exception e) {
			scanner.close();
		}

	}
}
