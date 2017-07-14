import cv2
import numpy as np

needsROI = True
needsHelperROI = True
def collectInput(event, x, y, flag, params):
    global xi, yi
    if event == cv2.EVENT_LBUTTONDOWN:
        print('xi: ' , x, ' yi: ', y )
        xi, yi = x, y
        global needsROI
        needsROI = False
        #print(needsROI)

def collectHelperInput(event, x, y, flag, params):
    global helperxi, helperyi
    if event == cv2.EVENT_LBUTTONDOWN:
        print('helperxi: ' , x, ' helperyi: ', y )
        helperxi, helperyi = x, y
        global needsHelperROI
        needsHelperROI = False
        #print(needsHelperROI)

cap0 = cv2.VideoCapture('capturelatency0630.MOV')

while True:
    ret, frame = cap0.read()
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL) #this reframes the window so it fits screen
    cv2.imshow('frame', frame)
    if needsROI == True and needsHelperROI == True:
        cv2.setMouseCallback('frame', collectInput)
    elif needsROI == False and needsHelperROI == True:
        cv2.setMouseCallback('frame', collectHelperInput)
    elif needsROI == False and needsHelperROI == False:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap0.release()
cv2.destroyAllWindows()
