import paho.mqtt.client as mqtt
import json
import time

def main():
    mqttBroker = "broker.hivemq.com"
    client = mqtt.Client("Sanitizing system") 

    client.username_pw_set("EA", "mqttBROKER") 
    connection_check(client, mqttBroker, 1883)     
    
    client.loop_start()
    client.on_connect = on_connect
    client.on_message = on_message
    time.sleep(5)
    client.disconnect()
    client.loop_stop()  

def connection_check(client,broker, port):
    try:
        client.connect(broker,port) 
    except:
        print("connection failed")

def on_connect(client, userdata, flags, rc):                  
    if rc==0:                                         
        client.connected_flag = True                  
        client.subscribe("owntracks/EA/#")            

def on_message(client,userdata,msg ):                 
    topic = msg.topic                                    
    try:                       
        data = json.loads(msg.payload.decode("utf8")) 
        lat = data['lat']
        long = data['lon']
        within_distance(lat,long)
    except:
        print ("Cannot decode data on topic {0}".format(topic))     

def within_distance(lat,long):
    while True:
        if 52.40<= lat <=52.41 and -1.50 <= long <= -1.49:         #suppose my home location is 52.409, -1.498
            print ("The client is still in home")
            time.sleep(10)
        else:
            print ("The client is out of home")
            break   

if __name__ == "__main__":
    main()