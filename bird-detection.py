import cv2
import numpy as np
# Read the original image
img = cv2.imread('oiseau pas belle.jpg') 
 
# Convert to graycsale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 
 
# Canny Edge Detection
edges = cv2.Canny(image=img_gray, threshold1=150, threshold2=200) # Canny Edge Detection
kernal = np.ones((2, 2), np.uint8)
dilation = cv2.dilate(edges, kernal, iterations=0)

contours, hierarchy = cv2.findContours(
    dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

objects = str(len(contours))
text = "Obj:"+str(objects)
cv2.putText(dilation, text, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
            0.4, (240, 0, 159), 1)

scale_percent = 100 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
resized = cv2.resize(dilation, dim, interpolation = cv2.INTER_AREA)
# Display Canny Edge Detection Image
# cv2.imshow('Original', img)
cv2.imshow('Dilation', resized)
print(text)
cv2.waitKey(0)
cv2.destroyAllWindows()
