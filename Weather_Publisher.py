import paho.mqtt.client as mqtt
import requests
import json

#The API key was generated from the OpenWeatherMap website
API_key = "2837c7dc12f0d19128fc0758d1f52efd"
mqttBroker = "broker.hivemq.com"
client = mqtt.Client("Weather System") #MQTT client initialisation

def on_connect(client, userdata, flags, rc):
    client.connect(mqttBroker, 1883)
    client.connected_flag = True
    print("Connected with weather system")

def main():
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat=52.41&lon=-1.51&cnt=1&appid={API_key}" #the coordinates for Coventry are (52.41, -1.51) and cnt is used to limit the number of results returned
    response = requests.get(url)
    data = response.json()
    for forecast in data["list"]: #the rain category is listed under the 'list' variable in the API response
        if 'rain' not in data or '3h' not in data['rain'] or float(data['rain']['3h']) == 0:
            return 1
    return 0
    print(data)

client.on_connect = on_connect

main()


if main() == 1: 
    client.publish("cleaning/trigger", 1) #the conditions indicate no rain in the next three hours, so a 1 is published
else:
    client.publish("cleaning/trigger", 0) #the conditions indicating it is or will rain have been set off, so a 0 is published
    time.sleep(3600 * 3) #checks again in three hours time

client.loop_forever() #keeps running the loop until the program ends
