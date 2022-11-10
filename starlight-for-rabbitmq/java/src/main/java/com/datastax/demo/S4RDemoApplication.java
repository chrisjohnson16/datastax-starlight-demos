package com.datastax.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.context.ApplicationContext;
import org.springframework.context.EnvironmentAware;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.ImportResource;
import org.springframework.core.env.Environment;

import lombok.Setter;

@Setter
@Configuration
@ImportResource("classpath:beans.xml")
public class S4RDemoApplication {

	public static void main(String[] args) {
		ApplicationContext applicationContext = SpringApplication.run(S4RDemoApplication.class, args);
		
		Demo demo = applicationContext.getBean(Demo.class);		
		try {
			demo.run();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	@Setter
	public static class Demo implements EnvironmentAware {
		private static String SEND = "send";
		private static String RECEIVE = "receive";
		
		private String action;
		private String location = "rabbit";
		private String exchange;
		private String queueName;
		private Sender sender;
		
		public void run() throws Exception {

			if (action.equals(SEND)) {
				if (exchange.equals("direct")) {
					System.out.println("Sending a " + exchange + " message to " + location + " queue " + queueName);
				}
				else if (exchange.equals("fanout")) {
					System.out.println("Sending a " + exchange + " message to " + location);					
				}
				sender.send();
			}
			else if (action.equals(RECEIVE)) {
				System.out.println("Receiving " + exchange + " messages from " + location + " queue " + queueName);		
			}
		}

		@Override
		public void setEnvironment(Environment environment) {

			if (environment.getActiveProfiles().length != 3) {
				throw new RuntimeException("Wrong number of active profiles.  Must be either 'send' or 'receive'");
			}

			exchange = environment.getActiveProfiles()[0];
			action = environment.getActiveProfiles()[1];
		}
		
	}
}
