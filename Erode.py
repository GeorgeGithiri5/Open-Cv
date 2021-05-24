import cv2
import numpy as np 

path = r'C:\Users\George\Desktop\Coding\Python\OpenCv\Untitled.png'

image = cv2.imread(path)

window_name = "Image"

kernel = np.ones((6, 6), np.uint8)

image = cv2.erode(image, kernel, cv2.BORDER_REFLECT)

cv2.imshow(window_name, image)