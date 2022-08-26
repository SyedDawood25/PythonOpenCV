import cv2 as cv

# reading and scaling images

img = cv.imread('cat2.jpg')
cv.imshow('Cat', img)

def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale) #frame.shape[1] is the width
    height = int(frame.shape[0] * scale) #frame.shape[0] is the height
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) #resizing the frame and returning it to the caller

resizedImage = rescaleFrame(img, scale = 0.25)
cv.imshow('Cat2', resizedImage)

cv.waitKey(0)

# reading and scaling videos

vid = cv.VideoCapture('cat.mp4')

def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale) #frame.shape[1] is the width
    height = int(frame.shape[0] * scale) #frame.shape[0] is the height
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) #resizing the frame and returning it to the caller

while True:
    isRead, frame = vid.read()

    resizedFrame = rescaleFrame(frame, scale = 0.25)
    cv.imshow('Video', resizedFrame)

    if cv.waitKey(25) & 0xFF == ord('q'):
        break

vid.release()
cv.destroyAllWindows()