import cv2

imagem_original = cv2.imread("images/leaves/leaf_02.png")
cols, lins, _ = imagem_original.shape
print(imagem_original.shape)
matriz = cv2.getRotationMatrix2D((cols / 2, lins / 2), 90, 1)
imagem_rotate90 = cv2.warpAffine(imagem_original, matriz, (cols, lins))

cv2.imshow("Resultado", imagem_rotate90)
cv2.imshow("Original", imagem_original)
cv2.waitKey(0)
cv2.destroyAllWindows()
