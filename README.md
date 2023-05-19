
# Zoom Any Picture Using Hand Gestures (python Opencv Project)

This project showcases a Python application that allows you to zoom in and out of any picture using hand gestures. It utilizes the OpenCV library along with the cvzone module to detect and track hand gestures, enabling you to control the zoom level of an image effortlessly.

let's start...............

To make this project you need to follow this step:-

## Installation

Install package with pip

```bash
pip install cvzone==1.4.1
pip install mediapipe==0.8.3.1

```
    
## Deployment

To deploy this project run

```bash
# Please Subscribe my youtube channel "@problemsolvewithridoy"

import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.7)

startDis = None
scale = 0
cx, cy = 200, 200

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    
    img1 = cv2.imread("one.jpg") # write your picture file name

    if len(hands) == 2:
        # print("Zoom Gesture")
        # print(detector.fingersUp(hands[0]), detector.fingersUp(hands[1]))
        hand1 = hands[0]
        hand2 = hands[1]

        hand1_fingers = detector.fingersUp(hands[0])
        hand2_fingers = detector.fingersUp(hands[1])

        if hand1_fingers == [1,1,0,0,0] and hand2_fingers == [1,1,0,0,0]:
            lmList1 = hand1["lmList"]
            lmList2 = hand2["lmList"]

            if startDis is None:
                # length, info, img = detector.findDistance(lmList1[8], lmList2[8], img)
                length, info, img = detector.findDistance(hand1["center"], hand2["center"], img)
                # print(length)
                startDis = length

            # length, info, img = detector.findDistance(lmList1[8], lmList2[8], img)
            length, info, img = detector.findDistance(hand1["center"], hand2["center"], img)
            scale = int((length - startDis)//2)
            cx, cy = info[4:]
            # print(scale)

    else:
        startDis = None
    
    try:
        h1, w1, _ = img1.shape
        newH, newW = ((h1 + scale)//2)*2 , ((w1 + scale)//2)*2
        img1 = cv2.resize(img1,(newH, newW))
        img[cy - newH//2 : cy + newH//2, cx - newW//2 : cx + newW//2] = img1
    
    except:
        pass
    
    

    cv2.imshow("Problem Solve with Ridoy", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```

## You can follow me

Facebook:- https://www.facebook.com/problemsolvewithridoy/

Linkedin:- https://www.linkedin.com/in/ridoyhossain/

YouTube:- https://www.youtube.com/@problemsolvewithridoy

Gmail:- entridoy2@gmail.com

If you have any confusion, please feel free to contact me. Thank you


## License
This script is released under the MIT License. Feel free to use, modify, and distribute it as you wish. If you find any bugs or have any suggestions for improvement, please submit an issue or a pull request on this repository.

