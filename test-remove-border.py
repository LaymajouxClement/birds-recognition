import cv2
import numpy as np

# read image
img = cv2.imread('hard.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY)[1]
kernel = np.ones((7,7),np.uint8)
kernel2 = np.ones((3,3),np.uint8)
marker = thresh.copy()
marker[1:-1,1:-1]=0
while True:
    tmp=marker.copy()
    marker=cv2.dilate(marker, kernel2)
    marker=cv2.min(thresh, marker)
    difference = cv2.subtract(marker, tmp)
    if cv2.countNonZero(difference) == 0:
        break

mask=cv2.bitwise_not(marker)
mask_color = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
out=cv2.bitwise_and(img, mask_color) 

scale_percent = 50 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# save cropped image
resized = cv2.resize(out, dim, interpolation = cv2.INTER_AREA)
    # Display Canny Edge Detection Image
    # cv2.imshow('Original', img)
cv2.imshow('Dilation', resized)
# show the images
cv2.waitKey(0)
cv2.destroyAllWindows()