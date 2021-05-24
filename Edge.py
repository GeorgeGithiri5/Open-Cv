import cv2
import numpy as np 

FILENAME = 'Untitled.png'

try:
	img = cv2.imread(FILENAME)
	edges = cv2.Canny(img, 100, 200)

	cv2.imwrite('Out.png', edges)

except IOError:
	print("Error while reading files !!!")