import cv2

cam = cv2.VideoCapture(0)

while True:
    ignore, frame = cam.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('WebCam1', frame)
    cv2.moveWindow('WebCam1', 0, 0)
    cv2.imshow('WebCam2', grayFrame)
    cv2.moveWindow('WebCam2', 640, 0)
    cv2.imshow('WebCam3', grayFrame)
    cv2.moveWindow('WebCam3', 0, 400)
    cv2.imshow('WebCam4', frame)
    cv2.moveWindow('WebCam4', 640, 400)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()