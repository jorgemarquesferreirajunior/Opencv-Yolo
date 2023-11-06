import cv2
# sobel: realça contornos

img_org = cv2.imread("images/places/parking.png")
img_bilateral = cv2.bilateralFilter(img_org, 9, 75, 75)
img_sobel_x = cv2.Sobel(img_bilateral, cv2.CV_8U, 1, 0, ksize=3)
img_sobel_x2 = cv2.Sobel(img_org, cv2.CV_8U, 1, 0, ksize=3)
img_sobel_y = cv2.Sobel(img_bilateral,cv2.CV_8U , 0, 1, ksize=3)
img_sobel_y2 = cv2.Sobel(img_org, cv2.CV_8U, 0, 1, ksize=3)

cv2.imshow("imagem_original", img_org)

cv2.imshow("img_sobel_x", img_sobel_x)
cv2.imshow("img_sobel_x2", img_sobel_x2)
cv2.imshow("img_sobel_y", img_sobel_y)
cv2.imshow("img_sobel_y2", img_sobel_y2)


cv2.waitKey(0)
cv2.destroyAllWindows()
