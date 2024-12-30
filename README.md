# Flask Service for Eureka Registration

This is a Flask service that registers itself with a Eureka server built in Spring Boot.

## Project Description

This project demonstrates how to create a Flask service that can register itself with a Eureka server. Eureka is a service registry that helps applications discover other services.

## How it Works

The Flask service registers itself with the Eureka server by sending a POST request to the `/eureka/apps/{service-name}` endpoint. The service also sends periodic heartbeats to the Eureka server to indicate that it is still alive.

## Code

The code for the Flask service is included in the `app.py` file. The code defines the following functions:

* `register_with_eureka`: This function registers the Flask service with the Eureka server.
* `send_heartbeat`: This function sends a heartbeat to the Eureka server.
* `home`: This function is the main entry point for the Flask service. It simply returns a message indicating that the service is running.

## Installation

Before running the Flask service, you need to install the required dependencies:

```bash
pip install flask requests

Markdown

# Flask Service for Eureka Registration

This is a Flask service that registers itself with a Eureka server built in Spring Boot.

## Project Description

This project demonstrates how to create a Flask service that can register itself with a Eureka server. Eureka is a service registry that helps applications discover other services.

## How it Works

The Flask service registers itself with the Eureka server by sending a POST request to the `/eureka/apps/{service-name}` endpoint. The service also sends periodic heartbeats to the Eureka server to indicate that it is still alive.

## Code

The code for the Flask service is included in the `app.py` file. The code defines the following functions:

* `register_with_eureka`: This function registers the Flask service with the Eureka server.
* `send_heartbeat`: This function sends a heartbeat to the Eureka server.
* `home`: This function is the main entry point for the Flask service. It simply returns a message indicating that the service is running.

## Installation

Before running the Flask service, you need to install the required dependencies:

```bash
pip install flask requests
Running the Service
1. Start the Eureka Server:

Ensure your Eureka server is running at http://localhost:8761.

2. Run the Flask Service: python app.py
This will start the Flask service on port 5000.