import paho.mqtt.client as mqtt
# MQTT client callback functions
def on_connect(client, userdata, flags, rc):
    print("connected with result code " +str(rc))
    client.subscribe("temperature")

def on_message(client, userdata, msg) :
    print (msg.topic+" "+str(msg.payload))
    temperature = float (msg.payload.decode())
    control_heating(temperature)

# Function to control the heating system
def control_heating (temperature):
    if temperature < 10:
        print("Turning on heating")
    elif temperature >= 15:
        print ("Turning off heating")

# MQTT client initialization
client = mqtt.Client("Heating")
client.connect("broker.hivemq.com", 1883, 60)

client.on_connect = on_connect
client.on_message = on_message

# Start the MQTT client loop
client.loop_forever()
