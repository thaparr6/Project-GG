import os
import time
import ssl
import json
import paho.mqtt.client as mqtt

# Set the OpenWeather API key and city ID as environment variables
OPENWEATHER_API_KEY = os.environ.get('2837c7dc12f0d19128fc0758d1f52efd')
OPENWEATHER_CITY_ID = os.environ.get('3333139')

# Set the MQTT broker and topic
MQTT_BROKER = 'broker.hivemq.com'
MQTT_PORT = 1883
MQTT_TOPIC = 'weather'

# Set the MQTT client ID and message
CLIENT_ID = f'openweather_{random.randint(0, 1000)}'
MESSAGE = f'Weather in {3333139}:\n'

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f'Connected to {broker.hivemq.com} with result code {rc}')
        client.subscribe(weather_system)
    else:
        print(f'Failed to connect with result code {rc}')

def on_message(client, userdata, message):'weather'
    global MESSAGE
    if message.topic == MQTT_TOPIC:
        data = json.loads(message.payload)
        if 'weather' in data:
            weather = data['weather'][0]['description']
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            MESSAGE += f'- Weather: {weather}\n'
            MESSAGE += f'- Temperature: {temp}K\n'
            MESSAGE += f'- Humidity: {humidity}%\n'
            print(MESSAGE)

def main():
    client = mqtt.Client(CLIENT_ID)
    client.on_connect = on_connect
    client.on_message = on_message
    client.tls_set(ca_certs=None, certfile=None, keyfile=None, tls_version=ssl.PROTOCOL_TLS)
    client.connect(broker.hivemq.com, 1883)
    client.loop_forever()

if __name__ == '__main__':
    main()
