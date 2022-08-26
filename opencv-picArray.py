import random
import cv2
import numpy as np

boxes = int(input('Please enter the number of boxes in checkerboard: '))

while True:
    width = 0
    height = 0
    color = 255
    frame = np.zeros([250, 250, 3], dtype=np.uint8)
    # frame[0:100,0:100] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    # frame[100:,100:] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    for i in range(boxes):
        for j in range(boxes):
            frame[width:width+int(250/boxes),height:height+int(250/boxes)] = (color, color, color)
            if color == 0:
                color += 255
            else:
                color -= 255
            width += int(250/boxes)
        width = 0
        height += int(250/boxes)

    cv2.imshow('MYPic', frame)
    if cv2.waitKey(1) == ord('q'):
        break
