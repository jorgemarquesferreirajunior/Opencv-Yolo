import cv2
# filtro passa baixa - suavisador - desfoque...
img = cv2.imread("images/animals/pigs01.jpeg")
img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

img_Gaussianblur = cv2.GaussianBlur(img, (5, 5), 0)# blur: desfoca a imagem

cv2.imshow("img", img)
cv2.imshow("img_Gaussianblur", img_Gaussianblur)
cv2.waitKey(0)
cv2.destroyAllWindows()
