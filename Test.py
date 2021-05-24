import cv2 
img = cv2.imread("Untitled.png", cv2.IMREAD_COLOR)
cv2.imshow("Cute Kitens", img)

cv2.waitKey()
cv2.destroyAllWindows()