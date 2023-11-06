import cv2

img = cv2.imread("C:/Users/Mi/Documents/GitHub/Opencv-Yolo/images/phone.jpg")
img = cv2.resize(img, (1280//2, 720//2))
cv2.imshow("Imagem", img)

cv2.waitKey(0)
