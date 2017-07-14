import cv2
import numpy as np
import userinput0 as user
#difference between capturelatency and warm_startup
#different icon roi
#different threshold for that icon

cap = cv2.VideoCapture('capturelatency0630.MOV')
framecount = 0
iteration = 0
capture = True



while True and iteration <= 10:
    framecount += 1
    ret, frame = cap.read()
    #roi = frame[586, 646] #[row][column]  roi for the circle (left of trash) icon
    #flashroi = frame[343,388] #roi for the camera icon

#the following rectangles are drawn to help the developer manually select the region of interest
    cv2.rectangle(frame, (user.xi - 8, user.yi - 8), (user.xi + 8, user.yi + 8), (255,0, 0), 2) #highlight region of interest
    cv2.rectangle(frame, (user.helperxi - 8, user.helperyi - 8), (user.helperxi + 8, user.helperyi + 8), (0, 255, 0), 2) #highlight the flash icon
    #flash icon is now the capture flag instead of phone icon because we never leave camera app


    roi = frame[user.yi, user.xi]
    helperroi = frame[user.helperyi, user.helperxi]

###### DISPLAY WINDOW
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL) #this reframes the window so it fits screen
    cv2.imshow('frame', frame)
#######################



    b, g, r = roi #[row][column]
    #print("framecount: ", framecount, "r: ",r ,"g: ",g,"b: ", b)

    b1, g1, r1 = helperroi
    print("framecount: ", framecount, "r1: ",r1 ,"g1: ",g1,"b1: ", b1)


    if r1 > 30 and g1 > 30 and b1 > 30: #we are looking at the right side of the shutter button
        capture = True

    if (r>=230 and g >= 230 and b >= 230 and capture == True):
        print(framecount)
        cv2.imwrite('endingframe%i.jpg' %framecount, frame)
        capture = False
        iteration += 1


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
