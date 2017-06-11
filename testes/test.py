import cv2

img = cv2.imread("test.jpg")
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(img_hsv)

print(h[0])
# cv2.imshow(h)
