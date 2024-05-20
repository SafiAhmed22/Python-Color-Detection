import cv2
import numpy 

cap=cv2.VideoCapture(0)
while True:
    ret, frame=cap.read()
    
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #detection for BLUE
    lower_blue=numpy.array([80,40,40])
    upper_blue=numpy.array([140,255,255])
    
    mask=cv2.inRange(hsv, lower_blue,upper_blue)
    result=cv2.bitwise_and(frame, frame, mask=mask)
    
    cv2.imshow("CAmERa",result)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()