import cv2

import os

image_path = r'C:\Users\George\Desktop\Coding\Python\OpenCv\Untitled.png'

directory = r'C:\Users\George\Desktop\Coding\Python'

img = cv2.imread(image_path)

os.chdir(directory)

print("Before saving image")

print(os.listdir(directory))

filename = "savedImage.png"

cv2.imwrite(filename, img)

print("After saving image")
print(os.listdir(directory))

print('Successfully saved')