import cv2

import numpy as np 

image1 = cv2.imread('Untitled.png')
image2 = cv2.imread('Untitled.png')

sub = cv2.subtract(image1, image2)

cv2.imshow('subtracted Image', sub)

if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()