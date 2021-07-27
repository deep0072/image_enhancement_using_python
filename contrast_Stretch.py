import cv2
from skimage.exposure import adjust_sigmoid
import numpy as np
# Reading the image.
img1 = cv2.imread('img4.png')
img1 = cv2.resize(img1, (1000,1000))

def trackbar(x):
    x = cv2.getTrackbarPos('contrast x', 'window')
    print(x)
    if x == 0:
        x == "normal"
        cv2.imshow('window', img1)
    else:

            
        # Applying Sigmoid correction.
        img2 = adjust_sigmoid(img1, gain=x)
        # Saving img2.
        print(img2.dtype)

    
        img2 = cv2.resize(img2, (1000,1000))
        h_img = cv2.hconcat([img1, img2])
        cv2.imshow('window', h_img)
       




cv2.namedWindow('window')
cv2.createTrackbar('contrast x', 'window', 6, 15, trackbar)


cv2.waitKey(0)
cv2.destroyAllWindows()