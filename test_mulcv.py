import numpy as np
import cv2

im = cv2.imread('source2.png')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
        if cv2.contourArea(c) <= 50 :
            continue    
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255,0), 2)
        center = (x,y)
        print (center)

while True: 
    cv2.imshow('test',im)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()