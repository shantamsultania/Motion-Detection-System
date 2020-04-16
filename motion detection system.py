import cv2
import numpy

camera = cv2.VideoCapture(0)

check, frame1 = camera.read()
check, frame2 = camera.read()

while True:
    difference = cv2.absdiff(frame1,frame2)
    gray = cv2.cvtColor(difference,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    check3, thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dialted = cv2.dilate(thresh,None, 3)
    objects, _ = cv2.findContours(dialted,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for obj in objects:
        (x,y,w,h)= cv2.boundingRect(obj)

        if cv2.contourArea(obj) < 700:
            continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow('frame',frame1)
    frame1 = frame2
    check, frame2 = camera.read()

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
camera.release()