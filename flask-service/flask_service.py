from flask import Flask
import requests
import socket
import threading
import time

app = Flask(__name__)

EUREKA_SERVER = "http://localhost:8761/eureka/apps"

# Flask service details
SERVICE_NAME = "FLASK-SERVICE"
SERVICE_PORT = 5000
HOST_NAME = socket.gethostname()
IP_ADDR = socket.gethostbyname(HOST_NAME)
INSTANCE_ID = f"{HOST_NAME}:{SERVICE_NAME}:{SERVICE_PORT}"


def register_with_eureka():
    """Registers the Flask service with Eureka."""
    eureka_url = f"{EUREKA_SERVER}/{SERVICE_NAME}"
    instance_info = {
        "instance": {
            "instanceId": INSTANCE_ID,
            "hostName": HOST_NAME,
            "app": SERVICE_NAME,
            "ipAddr": IP_ADDR,
            "vipAddress": SERVICE_NAME,
            "secureVipAddress": SERVICE_NAME,
            "status": "UP",
            "port": {"$": SERVICE_PORT, "@enabled": "true"},
            "dataCenterInfo": {
                "@class": "com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo",
                "name": "MyOwn"
            }
        }
    }

    headers = {"Content-Type": "application/json"}
    try:
        # Register the instance with Eureka
        response = requests.post(eureka_url, json=instance_info, headers=headers)
        if response.status_code == 204:
            print(f"Service {SERVICE_NAME} registered successfully with Eureka!")
        else:
            print(f"Failed to register service: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Error while registering with Eureka: {e}")


def send_heartbeat():
    """Sends a heartbeat to the Eureka server."""
    heartbeat_url = f"{EUREKA_SERVER}/{SERVICE_NAME}/{INSTANCE_ID}"
    headers = {"Content-Type": "application/json"}
    while True:
        try:
            response = requests.put(heartbeat_url, headers=headers)
            if response.status_code == 200:
                print(f"Heartbeat sent for {SERVICE_NAME}")
            else:
                print(f"Heartbeat failed: {response.status_code}, {response.text}")
        except Exception as e:
            print(f"Error while sending heartbeat: {e}")
        time.sleep(30)  # Send heartbeat every 30 seconds


@app.route("/")
def home():
    return "<h1>Flask Service is running and registered with Eureka!</h1>"


if __name__ == "__main__":
    # Register the service with Eureka
    threading.Thread(target=register_with_eureka).start()

    # Start sending heartbeats in a separate thread
    threading.Thread(target=send_heartbeat, daemon=True).start()

    # Start the Flask app
    app.run(port=SERVICE_PORT)
