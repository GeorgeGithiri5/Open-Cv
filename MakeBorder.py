import cv2

path = r'C:\Users\George\Desktop\Coding\Python\OpenCv\Untitled.png'

image = cv2.imread(path)

window_name = "Image"

image = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT)
cv2.imshow(window_name, image)