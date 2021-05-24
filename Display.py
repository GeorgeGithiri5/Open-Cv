import cv2

path = r'C:\Users\George\Desktop\Coding\Python\OpenCv\Untitled.png'

image = cv2.imread(path)

window_name = 'image'

cv2.imshow(window_name, image)

cv2.waitKey(0)

cv2.destroyAllWindows()