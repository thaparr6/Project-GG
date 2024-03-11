import paho.mqtt.client as mqtt
import time
import subprocess,os
import cv2, time, pandas
import datetime

#To capture the first frame and differences 
static_back = None
motion_list = [ None, None ]
#For when movement happens
time = []

df = pandas.DataFrame(columns = ["Start", "End"])
video = cv2.VideoCapture(0)


def main():
    mqttBroker = "broker.hivemq.com"
    client = mqtt.Client("##") 
    client.connect(mqttBroker,1883)      
    #This will open camera and check if there is motion
    subprocess.run('start microsoft.windows.camera:', shell=True)
    i = False
    count = 0
    while i == False:
        time.sleep(1)
        count = count + 1
        #Check for Motion
        
        #Send message it there is motion or not
        if i == True:
            print("The Process will not continue")
        elif count == 300:
            print("Process wil continue")
            break
        
    subprocess.run('Taskkill /IM WindowsCamera.exe /F', shell=True)
    client.publish("Motion",i)
    

    
    

if __name__ == "__main__":
    main()


