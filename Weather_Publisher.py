import paho.mqtt.client as mqtt
import requests
import json

#The API key was generated from the OpenWeatherMap website
API_key = "19b21c8ed496b716ea542ad051cfb170"
mqttBroker = "broker.hivemq.com"
client = mqtt.Client("Weather System") #MQTT client initialisation
client.on_connect = on_connect

def on_connect(client, userdata, flags, rc):
    client.connect(mqttBroker, 1883)
    client.connected_flag = True
    print("Connected with weather system")

def get_weather_forecast():
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat=52.41&lon=-1.51&appid={API_key}" #the coordinates for Coventry are (52.41, -1.51) and these are required for the API call
    response = requests.get(url)
    data = response.json()
    precipitation = 0 #initialise the variable
    for forecast in data["list"]: #the rain category is listed under the 'list' variable in the API response
        if 'rain' not in data or '3h' not in data['rain'] or float(data['rain']['3h']) == 0:
            return True
    return False

while True:
    if get_weather_forecast() == True: 
        client.publish("cleaning/trigger", 1) #the conditions indicate no rain in the next three hours, so a 1 is published
    else:
        client.publish("cleaning/trigger", 0) #the conditions indicating it is or will rain have been set off, so a 0 is published
    time.sleep(3600 * 3)

client.loop_forever() #keeps running the loop until the program ends
