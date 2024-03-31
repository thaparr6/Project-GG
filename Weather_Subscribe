import paho.mqtt.client as mqtt
import requests
import json
import time


def on_connect(client, userdata, flags, rc):
     client.connected_flag = True
     print("Connected with result code “+str(rc))
     client.subscribe(“Weather")

def on_message(client, userdata, msg):
     global next_spray_time

client = mqtt.Client(“Weather System”)
mqttBroker = “broker.hivemq.com”
client.connect(mqttBroker, 1883)

def main():
     api_key = “19b21c8ed496b716ea542ad051cfb170”
     forecast_url = f”http://api.openweathermap.org/data/2.5/forecast7q=Coventry&appid={api_key}”
     while True:
          response = requests.get(forecast_url)
          data = response.json()
          if ‘precipitation’ > 1: 
          # if there is going to be more than 1 millimetre of rain in the next three hours, the cleaning will be rescheduled   
          next_spray_time = time.time() + (3600 * 5) # next spray scheduled in 5 hours time
          print("Rescheduling spraying for later")
     else:
          print(“Start  spraying “)
          
     
          time.sleep(3600 * 5) 
     
     next_spray_time = time.time()

if __name__ == "__main__":
     main()

