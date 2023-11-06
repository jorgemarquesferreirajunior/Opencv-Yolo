import cv2
import numpy as np

imagemOriginal = cv2.imread("images/animals/pigs03.jpeg")

pontosIniciais = np.float32([[203, 137], [1211, 495], [5, 255], [1015, 875]])
pontosFinais = np.float32([[0, 0], [1000, 0], [0, 300], [1000, 300]])

matriz = cv2.getPerspectiveTransform(pontosIniciais, pontosFinais)

imagemModificada = cv2.warpPerspective(imagemOriginal, matriz, (1000, 300))

cv2.imshow("Original", imagemOriginal)
cv2.imshow("Modificada", imagemModificada)

cv2.waitKey(0)
cv2.destroyAllWindows()
