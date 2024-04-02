import paho.mqtt.client as mqtt

def main():
    mqttBroker = "broker.hivemq.com"
    client = mqtt.Client("Sanitizing System")
    client.on_connect = on_connect
    client.on_message = on_message

def on_connect(client,userdata,flags,rc):
    client.connected_flag = True
    client.connect(mqttBroker,1883)
    print("Connected with motion sensor")
    client.subscribe("Motion")
    
def detection(Motion):
    if Motion == True:
        print("The Process will not continue")
    elif Motion == False:
        print("Process wil continue")

def on_message(client,userdata,msg):
    motion = msg.payload.decode()
    detection(motion)

main()

