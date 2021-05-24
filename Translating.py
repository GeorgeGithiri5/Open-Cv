import cv2
import numpy as np 

FILE_NAME = "Untitled.png"

M = np.float32([[1, 0, 100], [0, 1, 50]])

try:
	img = cv2.imread(FILE_NAME)
	(rows, cols) = img.shape[:2]

	res = cv2.warpAffine(img, M, (cols, rows))

	cv2.imwrite('output.png', res)
except IOError:
	print("Error while reading files!!")