import cv2
import numpy as np

#my plan for this is just to capture the ending frame, and write to a file

#
# designate a region of interest (use a previous warm start as reference)
# while True and count (iteration) <= 10
# check region of interest for BGR threshold
# if threshold met, save frame number and the frame itself
#
#
#
#








cap = cv2.VideoCapture('warm_startup.MOV')
framecount = 0
iteration = 0
starting = True
ending = False
capture = True
while True and iteration <= 10:
    framecount += 1
    ret, frame = cap.read()
    roi = frame[263, 308] #[row][column]

    cv2.rectangle(frame, (300,255), (316,271), (0, 255, 0), 2) #highlight region of interest

    cv2.namedWindow('frame', cv2.WINDOW_NORMAL) #this reframes the window so it fits screen
    cv2.imshow('frame', frame)

    b, g, r = roi #[row][column]
    print("framecount: ", framecount, "r: ",r ,"g: ",g,"b: ", b)

    if r>130 and g > 130 and b > 150 and r < 150 and g < 150 and b < 170:
        print(framecount)
        cv2.imwrite('endingframe%i.jpg' %framecount, frame)
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
