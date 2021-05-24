import cv2
import numpy as np 

FILE_NAME = 'Untitled.png'

try:
	img = cv2.imread(FILE_NAME)
	(rows, cols) = img.shape[:2]

	M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
	res = cv2.warpAffine(img, M, (cols, rows))

	cv2.imwrite('result.png', res)

except IOError:
	print('Error while reading files!!')