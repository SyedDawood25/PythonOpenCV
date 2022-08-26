import cv2 as cv

img = cv.imread('cat2.jpg')

def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale) #frame.shape[1] is the width
    height = int(frame.shape[0] * scale) #frame.shape[0] is the height
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) # interpolation in inter area is useful when shrinking the image
    # return cv.resize(frame, dimensions, interpolation=cv.INTER_LINEAR) # interpolation in inter linear is useful when enlarging the image
    # return cv.resize(frame, dimensions, interpolation=cv.INTER_CUBIC) # interpolation in inter cubic is useful when enlarging the image with higher quality but slower

# Normal Picture
resized = rescaleFrame(img, 0.35)
cv.imshow('NormalCat', resized)

# Change the color type of image
grayScale = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow('GrayScaleCat', grayScale)

# Blur the image
blurred = cv.GaussianBlur(resized, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('Blurred Cat', blurred)

# Edge Cascading on the image
canny = cv.Canny(resized, 175, 185)
cv.imshow('Edge Canny', canny)

# Dilating the Image
dilated = cv.dilate(canny, (7, 7), iterations=1)
cv.imshow('Dilated Image', dilated)

# Eroding the Image
eroded = cv.erode(dilated, (7, 7), iterations=1)
cv.imshow('Eroded Image', eroded)

# Cropping the Image
cropped = resized[0:200, 0:400]
cv.imshow('Cropped Image', cropped)

cv.waitKey(0)