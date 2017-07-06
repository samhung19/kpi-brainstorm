import cv2
import numpy as np

#contributors: Sam Hung & Josh Zeng
# this program allows the user to capture the ending frames (snapshot and frame number)
# when given an input file of startup latency (warm) from the Walleye device.


#my plan for this is just to capture the ending frame, and write to a file
#
# designate a region of interest (use a previous warm start as reference)
# while True and count (iteration) <= 10
# check region of interest for BGR threshold
# if threshold met, save frame number and the frame itself
#
#
# next thing, check to see if the data gathered from the first run aligns with
# the data when taken manually -- if so, this is a good sign. we can then
# move onto capturing the starting frame

cap = cv2.VideoCapture('warm_startup.MOV')
framecount = 0
iteration = 0
capture = True


while True and iteration <= 10:
    framecount += 1
    ret, frame = cap.read()
    roi = frame[263, 308] #[row][column]  roi for the flash icon
    phoneroi = frame[518,702] #roi for the camera icon

#the following rectangles are drawn to help the developer manually select the region of interest
    cv2.rectangle(frame, (300,255), (316,271), (0, 255, 0), 2) #highlight region of interest
    cv2.rectangle(frame, (694, 510), (710, 526), (0, 0, 255), 2) #highlight the phone icon



###### DISPLAY WINDOW
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL) #this reframes the window so it fits screen
    cv2.imshow('frame', frame)
#######################

    b, g, r = roi #[row][column]
    #print("framecount: ", framecount, "r: ",r ,"g: ",g,"b: ", b)

    b1, g1, r1 = phoneroi
    #print("framecount: ", framecount, "r: ",r1 ,"g: ",g1,"b: ", b1)


    if r1 < 20 and g1 < 30 and b1 > 220:
        capture = True # capture can only be true again if phone icon exists (check for blue in that area)

    if r>130 and g > 130 and b > 150 and r < 150 and g < 150 and b < 170 and capture == True:
        print(framecount)
        cv2.imwrite('endingframe%i.jpg' %framecount, frame)
        capture = False
        iteration += 1


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
