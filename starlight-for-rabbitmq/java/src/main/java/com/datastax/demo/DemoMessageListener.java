package com.datastax.demo;

import org.springframework.amqp.core.Message;
import org.springframework.amqp.core.MessageListener;
import org.springframework.amqp.core.Queue;

import lombok.Setter;

@Setter
public class DemoMessageListener implements MessageListener {
	
	public DemoMessageListener(Queue queue)  {
		System.out.println("Creating listener for queue " + queue.getName() + ".");
	}
	
	public void onMessage(Message message) {

		String text = new String(message.getBody());
		System.out.println("[x] Received: " + text);
		
		if (text.equals("error")) {
			System.out.println("error in message!");
			throw new RuntimeException("error in message");
		}
	}

}
