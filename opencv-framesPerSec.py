import cv2
import time

FPSText = ''
width = 640
height = 360
frames = 0
currentFPS = 0
prevTime = time.time()

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore, frame = cam.read()

    currentFPS = int(1/(time.time()-prevTime))
    prevTime = time.time()
    FPSText = f'FPS: {currentFPS}'

    cv2.rectangle(frame, (0, 0), (150, 50), (255, 0, 0), 2)
    cv2.putText(frame, FPSText, (10, 35), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)

    cv2.imshow('WebCam1', frame)
    cv2.moveWindow('WebCam1', 0, 0)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()