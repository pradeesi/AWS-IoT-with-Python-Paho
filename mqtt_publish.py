# Import package
import paho.mqtt.client as mqtt
import ssl
import time

# Define Variables
MQTT_PORT = 8883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "helloTopic"
MQTT_MSG = "hello MQTT"

MQTT_HOST = "put your Custom Endpoint here"
CA_ROOT_CERT_FILE = "put AWS IoT Root Certificate File Name here"
THING_CERT_FILE = "put your Thing's Certificate File Name here"
THING_PRIVATE_KEY = "put your Thing's Private Key File Name here"


# Define on_publish event function
def on_publish(client, userdata, mid):
	print "Message Published..."


# Initiate MQTT Client
mqttc = mqtt.Client()

# Register publish callback function
mqttc.on_publish = on_publish

# Configure TLS Set
mqttc.tls_set(CA_ROOT_CERT_FILE, certfile=THING_CERT_FILE, keyfile=THING_PRIVATE_KEY, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

# Connect with MQTT Broker
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)		
mqttc.loop_start()

counter = 0
while True:
	mqttc.publish(MQTT_TOPIC,MQTT_MSG + str(counter),qos=1)
	counter += 1
	time.sleep(1)

# Disconnect from MQTT_Broker
# mqttc.disconnect()