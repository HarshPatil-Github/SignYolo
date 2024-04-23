from ultralytics import YOLO
import cv2
import math 
from gtts import gTTS
import time 
import os
# start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# model
model = YOLO("runs/detect/train11/weights/best.pt")

# object classes
classNames = [ "अ", "आ", "इ", "ई", "उ", "ऊ", "ए", "ऐ", "ओ", "औ", "क", "ख",
               "ग", "घ", "च", "छ", "ज", "झ", "ट", "ठ", "ड", "ढ", "ण", "त", "थ",
               "द", "ध", "न", "प", "फ", "ब", "भ", "म", "य", "र", "ल", "व", "श", 
               "स", "ह", "ळ", "क्ष", "ज्ञ", "१", "२", "३", "४", "५", "६", "७", "८", "९", "१०" ]


while True:
    success, img = cap.read()
    results = model(img, stream=True)

    # coordinates
    for r in results:
        boxes = r.boxes

        for box in boxes:
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

            # put box in cam
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # confidence
            confidence = math.ceil((box.conf[0]*100))/100
            print("Confidence --->",confidence)

            # class name
            cls = int(box.cls[0])
            print("Class name -->", classNames[cls])
            # convert class name to speech
            tts = gTTS(text=classNames[cls], lang='mr')  # 'mr' is the language code for Marathi
            tts.save("class_name.mp3")
            os.system("mpg321 class_name.mp3")

            # object details
            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2

            cv2.putText(img, classNames[cls], org, font, fontScale, color, thickness)
            time.sleep(0.5) 
    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()