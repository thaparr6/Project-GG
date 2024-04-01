import paho.mqtt.client as mqtt
import requests
import json
import time

#The API key was generated from the OpenWeatherMap website
API_key = "19b21c8ed496b716ea542ad051cfb170"
mqttBroker = "broker.hivemq.com"
client = mqtt.Client("Weather System") #MQTT client initialisation

def on_connect(client, userdata, flags, rc):
    client.connect(mqttBroker, 1883)
    client.connected_flag = True #ensures connection
    print("Connected with weather system")

def main():
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat=52.41&lon=-1.51&cnt=1&appid={API_key}" #the coordinates for Coventry are (52.41, -1.51) and cnt is used to limit the number of results returned
    response = requests.get(url)
    data = response.json()
    if "list" not in data or "rain" not in data["list"][0]: #checks whether the keyword 'rain' isn't present, indicating there is no rain forecast for the next three hours
        return 1

    if float(data["list"][0]["rain"]["3h"]) == 0:
        return 1
        
    return 0 #if the 'rain' keyword is present in the API response, or its value is greater than 0, this means it will rain and a 0 is returned

client.on_connect = on_connect

main()


if main() == 1: 
    client.publish("cleaning/trigger", 1) #the conditions indicate no rain in the next three hours, so a 1 is published
    print("no rain")
elif main() == 0:
    client.publish("cleaning/trigger", 0) #the conditions indicating it is or will rain have been set off, so a 0 is published
    print("rain")
    time.sleep(3600 * 3) #waits for three hours 

