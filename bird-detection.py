import cv2
import numpy as np
# Read the original image
# example of images 
#
# img = cv2.imread('ez.webp') 
# img = cv2.imread('test.jpg')
# img = cv2.imread('hard.jpg')
img = cv2.imread('grue.jpg')
# img = cv2.imread('test02.jpg')
# img = cv2.imread('Pigeon.jpg')
#=========================================

# Convert to graycsale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 

# Canny Edge Detection
edges = cv2.Canny(image=img_blur, threshold1=10, threshold2=200) # Canny Edge Detection

kernal = np.ones((2, 2), np.uint8)

dilation = cv2.dilate(edges, kernal, iterations=2) # dilatation 
erosion = cv2.erode(dilation,kernel=kernal,iterations=2) #erosion

contours, hierarchy = cv2.findContours(
    erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # find countours

erosion = cv2.fillPoly(erosion,pts=contours,color=(255,255,255)) # fill countours in white 

erosion = cv2.erode(erosion,kernel=kernal,iterations=1) # erode , remove the countours
contours, _ = cv2.findContours(
    erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) # detection N°2 

objects = str(len(contours))    # objects : String that countains the number of counted birds
text = "Obj:"+str(objects)      
cv2.putText(erosion, text, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
            0.4, (240, 0, 159), 1) # put text in the img

scale_percent = 60 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
resized = cv2.resize(erosion, dim, interpolation = cv2.INTER_AREA) # resized img of the result
# Display Canny Edge Detection Image
# cv2.imshow('Original', img)
cv2.imshow('image', resized) # show the result
print(text) # show in terminal the number of counted birds

cv2.waitKey(0) # wait for user before exiting
cv2.destroyAllWindows() # destroy all windows

#============================ END ===============================
