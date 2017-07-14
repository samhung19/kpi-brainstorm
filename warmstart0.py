import cv2
import numpy as np
import userinput0 as user
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
# UPDATE: changed roi from [263,308] to [265,308]


#cap = cv2.VideoCapture('warm_startup.MOV')

cap = cv2.VideoCapture('warm_startup.MOV')
framecount = 0
iteration = 0
capture = True

b_lag = 0
r_lag = 0
g_lag = 0



while True and iteration <= 10:
    framecount += 1
    ret, frame = cap.read()

    db = False
    dg = False
    dr = False
#orig warmstart ROI
    #roi = frame[265, 308] #[row][column]  roi for the flash icon
    #phoneroi = frame[518,702] #roi for the camera icon

    #the following rectangles are drawn to help the developer manually select the region of interest
    #cv2.rectangle(frame, (300,255), (316,273), (0, 257, 0), 2) #highlight region of interest
    #cv2.rectangle(frame, (694, 510), (710, 526), (0, 0, 255), 2) #highlight the phone icon

#warmstart1 roi
    #roi = frame[352, 396]
    #phoneroi = frame[568,762]
    #cv2.rectangle(frame, (386,344), (402,360), (0, 257, 0), 2) #highlight region of interest
    #cv2.rectangle(frame, (754, 560), (770, 576), (0, 0, 255), 2) #highlight the phone icon
    roi = frame[user.yi, user.xi]
    phoneroi = frame[user.helperyi, user.helperxi]




###### DISPLAY WINDOW
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL) #this reframes the window so it fits screen
    cv2.imshow('frame', frame)
#######################

    if framecount >= 2:
        b_lag = b
        g_lag = g
        r_lag = r

    b, g, r = roi #[row][column]

    if framecount == 1:
        b_lag = b
        g_lag = g
        r_lag = r

    db_val = int(b) - int(b_lag)
    dg_val = int(g) - int(g_lag)
    dr_val = int(r) - int(r_lag)
    if db_val > 120 and db_val < 200:
        db = True
    if dr_val > 120 and dr_val < 200:
        dr = True
    if dg_val > 120 and dg_val < 200:
        dg = True

    print("framecount: ", framecount, "r: ",r ,"g: ",g,"b: ", b)
    print(dr_val," ", dg_val, " ", db_val)
    b1, g1, r1 = phoneroi
    #print("framecount: ", framecount, "r: ",r1 ,"g: ",g1,"b: ", b1)


    if r1 < 20 and g1 < 30 and b1 > 220:
        capture = True # capture can only be true again if phone icon exists (check for blue in that area)

    #if (r>155 and g > 155 and b > 160 and r < 200 and g < 200 and b < 210 and capture == True) or (r > 100 and g > 105 and b > 110 and r < 120 and g < 120 and b < 130 and capture == True):
    if(db == True and dr == True and dg == True and capture == True):
        print(framecount)
        cv2.imwrite('endingframe%i.jpg' %framecount, frame)
        capture = False
        db = False
        dg = False
        dr = False
        iteration += 1


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
