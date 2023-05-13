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
    
    img1 = cv2.imread("one.jpg")

    if len(hands) == 2:
        # print("Zoom Gesture")
        # print(detector.fingersUp(hands[0]), detector.fingersUp(hands[1]))
        hand1 = hands[0]
        hand2 = hands[1]

        hand1_fingers = detector.fingersUp(hands[0])
        hand2_fingers = detector.fingersUp(hands[1])
    
    

    cv2.imshow("Problem Solve with Ridoy", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break