import cv2 as cv
import numpy as np

width = height = 500

frame = np.zeros([width, height, 3], dtype="uint8")

# Displaying text and aligning it within the frame
def putTextCenter(_str, font = cv.FONT_HERSHEY_PLAIN, sizeMultiplier = 1, thickness = 1):
    retVal, baseLine = cv.getTextSize(_str, font, sizeMultiplier, thickness)
    if width > retVal[0]:
        remSpace = width - retVal[0]
    else:
        print("SIZE EXCEEDED FRAME!")
        remSpace = 0
    cv.putText(frame, _str, (int(remSpace/2), int(height/2)), font, sizeMultiplier, (0,0,255), thickness)

putTextCenter("Hello its me Syed Dawood", 2)

# Displaying shapes and aligning them within the frame
cv.rectangle(frame, (0, 0), (250, 250), (255, 0, 0), -1)
cv.rectangle(frame, (250, 0), (500, 250), (0, 0, 255), -1)
cv.rectangle(frame, (0, 250), (250, 500), (0, 0, 0), -1)
cv.rectangle(frame, (250, 250), (500, 500), (0, 255, 255), -1)
cv.line(frame, (0, 0), (width, height), (255, 255, 255), 2)
cv.line(frame, (500, 0), (0, height), (255, 255, 255), 2)
cv.circle(frame, (int(width/2), int(height/2)), 40, (0, 255, 0), -1)
cv.circle(frame, (int(width/2), int(height/2)), 20, (255, 0, 255), -1)

cv.imshow('selfMadePic', frame)

cv.waitKey(0)