import cv2
import numpy as np

step = 0

def collectInput(event, x, y, flag, params):
    global xi, yi
    if event == cv2.EVENT_LBUTTONDOWN:
        print('xi: ' , x, ' yi: ', y )
        xi, yi = x, y
        global step
        step = 2

def collectInput2(event, x, y, flag, params):
    global xi2, yi2
    if event == cv2.EVENT_LBUTTONDOWN:
        print('xi2: ' , x, 'yi2: ', y )
        xi2, yi2 = x, y
        global step
        step = 3

def collectHelper(event, x, y, flag, params):
    global helperxi, helperyi
    if event == cv2.EVENT_LBUTTONDOWN:
        print('helperxi: ' , x, ' helperyi: ', y )
        helperxi, helperyi = x, y
        global step
        step = 1



cap0 = cv2.VideoCapture('warm_startup.MOV')

while True:
    ret, frame = cap0.read()
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL) #this reframes the window so it fits screen
    cv2.imshow('frame', frame)
    if step == 0:
        cv2.setMouseCallback('frame', collectHelper)
    elif step == 1:
        cv2.setMouseCallback('frame', collectInput)
    elif step == 2:
        cv2.setMouseCallback('frame', collectInput2)
    elif step >= 3:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap0.release()
cv2.destroyAllWindows()
