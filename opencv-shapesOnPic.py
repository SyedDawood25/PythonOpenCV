import cv2

myText = 'Dawood is the Best!'
width = 640
height = 360
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore, frame = cam.read()

    # frame[180:260, 280:360] = (0, 0, 0) -> One Way to do it
    # cv2.rectangle(frame, (280, 180), (360, 260), (255, 0, 0), -1) #Another easier way to do it
    # cv2.circle(frame, (int(width/2), int(height/2)+50), 50, (255, 0, 0), -1) #For a circle
    # cv2.putText(frame, myText, (150, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2) #Text on image

    cv2.imshow('MyWebCam', frame)
    cv2.moveWindow('MyWebCam', 0, 0)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()