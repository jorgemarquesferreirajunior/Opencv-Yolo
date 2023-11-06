import cv2
# melhora a imagem no centro -  redução no ruído preservando a nitidez das bordas
# e contornos
img = cv2.imread("images/objects/50cent.png")
img_bilateral_filter = cv2.bilateralFilter(img, 9, 75, 75)

cv2.imshow("original", img)

cv2.imshow("img_bilateral_filter", img_bilateral_filter)


cv2.waitKey(0)
cv2.destroyAllWindows()
