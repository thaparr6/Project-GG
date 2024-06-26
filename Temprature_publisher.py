import time 
import random
import paho.mqtt.client as mqtt

# MOTT client callback functions
def on_connect(client, userdata, flags, rc) :
    print ("Connected with result code "+str(rc))

# MQTT client initialization
client = mqtt. Client ()
client.on_connect = on_connect

# Connect to HivelO broker
client.connect("broker.hivemq.com", 1883, 60)

# Main loop
temperature = random.uniform(10, 30)
message = f"Temperature: {temperature: .1f} C"
client.publish("temperature", message)
print (message)
time.sleep(1)
