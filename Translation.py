import cv2
import numpy as np

imagem_original = cv2.imread("images/leaves/leaf_02.png")
cols, lins, _ = imagem_original.shape


matriz = np.float32([[1, 0, 100], [1, 0, 100]])
imagem_deslocada = cv2.warpAffine(imagem_original, matriz, (cols, lins))

cv2.imshow("Original", imagem_original)
cv2.imshow("Deslocada", imagem_deslocada)

cv2.waitKey(0)
cv2.destroyAllWindows()
