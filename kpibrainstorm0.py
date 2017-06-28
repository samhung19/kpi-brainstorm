import cv2
import numpy as np

cap = cv2.VideoCapture('lalalala.mp4')
framecount = 0
while True:
    framecount += 1
    ret, frame = cap.read()
    roi = frame[65:75, 985:995]

    cv2.rectangle(frame, (982,62), (998,78), (0, 255, 0), 2) #highlight region of interest

    cv2.namedWindow('frame', cv2.WINDOW_NORMAL) #this reframes the window so it fits screen
    cv2.imshow('frame', frame)

    b, g, r = frame[70][990] #[row][column]
    print("framecount: ", framecount, "r: ",r ,"g: ",g,"b: ", b)

    if r>250 and g > 250 and b > 250:
        print(framecount)
        cv2.imwrite('frame%i.jpg' %framecount, frame)
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
