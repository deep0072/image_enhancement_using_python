import cv2
import matplotlib.pyplot as plt
import numpy as np
# Opening the image.
a = cv2.imread('img4.png')
a = cv2.resize(a, (480,480))

def trackbar(x):

    gamma = x
    # b is converted to type float.
    b1 = a.astype(float)
    # Maximum value in b1 is determined.
    b3 = np.max(b1)
    # b1 is normalized
    b2 = b1/b3
    # gamma-correction exponent is computed.
    b4 = np.log(b2)*gamma
    # gamma-correction is performed.
    c = np.exp(b4)*255.0
    # c is converted to type int.
    c1 = c.astype(np.uint8)
    c1 = cv2.resize(c1, (480,480))
    print(c1.dtype)
    # Displaying c1
    # h_img = cv2.hconcat([c1, a])
    cv2.imshow("test", c1)


# cv2.imshow('window', a)
cv2.namedWindow('test')
cv2.createTrackbar('blur x', 'test', 1, 3, trackbar)


cv2.waitKey(0)
cv2.destroyAllWindows()