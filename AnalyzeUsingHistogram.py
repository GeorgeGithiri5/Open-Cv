import cv2
import matplotlib.pyplot as plt 

img = cv2.imread('Untitled.png', 0)

histr = cv2.calcHist([img], [0], None, [256], [0, 256])

# plt.plot(histr)
plt.hist(img.ravel(), 256, [0, 256])
plt.show()