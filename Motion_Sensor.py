import paho.mqtt.client as mqtt
import time
import subprocess,os
import cv2, time, pandas
import datetime

static_back = None
time = []
df = pandas.DataFrame(columns = ["Start", "End"])
video = cv2.VideoCapture(0)
i = False
count = 0

def main():
    static_back = None
    time = []
    df = pandas.DataFrame(columns = ["Start", "End"])
    video = cv2.VideoCapture(0)
    i = False
    count = 0
    mqttBroker = "broker.hivemq.com"
    client = mqtt.Client("##") 
    client.connect(mqttBroker,1883)      
    while True:
        #Check for Motion
        count = count + 1
        check, frame = video.read()
        motion = 0

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if static_back is None: 
                static_back = gray 
                continue

        diff_frame = cv2.absdiff(static_back, gray)  
        thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1] 
        thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2) 

        cnts,_ = cv2.findContours(thresh_frame.copy(), 
                                        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 

        for contour in cnts: 
                if cv2.contourArea(contour) < 10000: 
                        continue
                motion = 1
                (x, y, w, h) = cv2.boundingRect(contour) 
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                i = True

        cv2.imshow("Color Frame", frame)  
        if i == True or count == 200 :  
                if motion == 1: 
                        time.append(datetime.now()) 
                break
    #Send message it there is motion or not
    if i == True:
        print("The Process will not continue")
    elif count == 300:
        print("Process wil continue")
    client.publish("Motion",i)
    video.release() 
    cv2.destroyAllWindows()

    
    

if __name__ == "__main__":
    main()

    

if __name__ == "__main__":
    main()


