import cv2
import numpy as np

imagem_original = cv2.imread("images/leaves/leaf_02.png")

imagem_reduzida = cv2.resize(imagem_original, None, fx=0.5, fy=0.5, interpolation= cv2.INTER_CUBIC)
imagem_ampliada = cv2.resize(imagem_original, None, fx=2, fy=2, interpolation= cv2.INTER_CUBIC)
cv2.imshow("Ampliado", imagem_ampliada)
cv2.imshow("Original", imagem_original)
cv2.imshow("Reduzido", imagem_reduzida)
cv2.waitKey(0)
cv2.destroyAllWindows()
