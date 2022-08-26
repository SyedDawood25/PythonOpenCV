import cv2

width = 500
height = 500
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore, frame = cam.read()
    cv2.imshow('WebCam1', frame)
    cv2.moveWindow('WebCam1', 0, 0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()