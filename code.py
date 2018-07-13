# Python program for Detection of a 
# specific color(blue here) using OpenCV with Python
import cv2
import numpy as np 
import imutils
import pytesseract

# Webcamera no 0 is used to capture the frames
cap = cv2.VideoCapture(0) 
 
# This drives the program into an infinite loop.
# Captures the live stream frame-by-frame
_, frame = cap.read() 
# Converts images from BGR to HSV
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
lower_red = np.array([0,0,0])
upper_red = np.array([0,255,255])

# Here we are defining range of bluecolor in HSV
# This creates a mask of white coloured 
# objects found in the frame.
mask = cv2.inRange(hsv, lower_red, upper_red)

# The bitwise and of the frame and mask is done so 
# that only the blue coloured objects are highlighted 
# and stored in res
res = cv2.bitwise_and(frame,frame, mask= mask)
# Blur the image
res = cv2.GaussianBlur(res,(13,13), 0)
# Edge detection
edged = cv2.Canny(res, 100, 200)
# Dilate it , number of iterations will depend on the image
dilate = cv2.dilate(edged, None, iterations=4)
# perform erosion
erode = cv2.erode(dilate, None, iterations=4)

# make an empty mask 
mask2 = np.ones(frame.shape[:2], dtype="uint8") * 255

# find contours
cnts = cv2.findContours(erode.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]

orig = frame.copy()
for c in cnts:
    # if the contour is not sufficiently large, ignore it
    if cv2.contourArea(c) < 600:
        cv2.drawContours(mask2, [c], -1, 0, -1)
        continue
    
# Remove ignored contours
newimage = cv2.bitwise_and(erode.copy(), dilate.copy(), mask=mask2)
# Again perform dilation and erosion
newimage = cv2.dilate(newimage,None, iterations=7)
newimage = cv2.erode(newimage,None, iterations=5)
ret,newimage = cv2.threshold(newimage,0,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

# Tesseract OCR
temp = pytesseract.image_to_string(newimage)

# It will turn 3 digits in this case,
new = temp[0] + temp[1] + "." + temp[2]

# Write results on the image
cv2.putText(frame, new, (50,100), cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0,255,255), 2)


# Show the output
cv2.imshow('frame',frame)
cv2.imshow('orig',newimage)

cv2.waitKey(0)
cv2.destroyAllWindows()
 
# release the captured frame
cap.release()
