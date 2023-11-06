import cv2

# suavisa efeito sal e pimenta
imgOrig = cv2.imread("images/people/imagem08.png")

img_media_blur = cv2.medianBlur(imgOrig,5)
img_Gaussianblur = cv2.GaussianBlur(imgOrig, (5, 5), 0)# blur: desfoca a imagem

cv2.imshow("Imagem original", imgOrig)
cv2.imshow("Imagem mediaBlur", img_media_blur)
cv2.imshow("Imagem Gaussianblur", img_Gaussianblur)


cv2.waitKey(0)
cv2.destroyAllWindows()
