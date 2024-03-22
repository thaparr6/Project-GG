import paho.mqtt.client as mqtt
import cv2, time, pandas 
from datetime import datetime

#These value will be used in the loop to keep track of thvideo and time
static_back = None
time = []
video = cv2.VideoCapture(0)
i = False
count = 0

def main():
    mqttBroker = "broker.hivemq.com"
    client = mqtt.Client("Sanitizing System") 
    client.connect(mqttBroker,1883)      

    #Send message it there is motion or not
    if i == True:
        print("The Process will not continue")
    elif count == 300:
        print("Process wil continue")
    client.publish("Motion",i)

while True:
        count = count + 1
        check, frame = video.read() 

        motion = 0
        #Will convert video to grayscale then to GaussianBlur
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        #This is the first fram 
        if static_back is None: 
                static_back = gray 
                continue

        #The difference between starting frame and current
        diff_frame = cv2.absdiff(static_back, gray)
        #If change bigger than 50 it will shown as white
        white_frame = cv2.threshold(diff_frame, 50, 255, cv2.THRESH_BINARY)[1] 
        white_frame = cv2.dilate(white_frame, None, iterations = 2) 

        cnts,_ = cv2.findContours(white_frame.copy(), 
                                        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 

        for contour in cnts: 
                if cv2.contourArea(contour) < 10000: 
                        continue
                motion = 1

                (x, y, w, h) = cv2.boundingRect(contour) 
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                i = True
        #It will display a frame as if it was a webcam 
        cv2.imshow("Color Frame", frame)
        key = cv2.waitKey(1)
        if i == True:
                if motion == 1: 
                        time.append(datetime.now()) 
                break
        if count == 300:
                if motion == 1:
                        time.append(datetime,now())
                break    
video.release() 
cv2.destroyAllWindows()    

if __name__ == "__main__":
    main()



