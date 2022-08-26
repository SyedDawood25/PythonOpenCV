import cv2

rows = int(input('Enter how many rows: '))
cols = int(input('Enter how many columns: '))

width = 1366
height = 768
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore, frame = cam.read()
    frame = cv2.resize(frame, (int(width/cols), int(height/cols)))
    for i in range(rows):
        for j in range(cols):
            cv2.imshow('WebCam'+str(i)+'x'+str(j), frame)
            cv2.moveWindow('WebCam'+str(i)+'x'+str(j), int(width/cols)*j, int(height/cols+30)*i)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()