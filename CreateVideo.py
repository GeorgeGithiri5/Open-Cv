import os
import cv2
from PIL import Image

print(os.getcwd())

os.chdir("C:\\Users\\George\\Desktop\\Coding\\Python\\OpenCv")
path = "C:\\Users\\George\\Desktop\\Coding\\Python\\OpenCv"

mean_height = 0
mean_width = 0

num_of_images = len(os.listdir('.'))

for file in os.listdir('.'):
	im = Image.open(os.path.join(path, file))
	width, height = im.size
	mean_width += width
	mean_height += height

mean_width = int(mean_width/num_of_images)
mean_height = int(mean_height/num_of_images)

for file in os.listdir('.'):
	if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
		im = image.open(os.path.join(path, file))
		width, height = im.size
		print(width, height)

		