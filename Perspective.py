import cv2
import numpy as np

imagemOriginal = cv2.imread("images/games/sudoku.png")

cv2.imshow("Original", imagemOriginal)

pontosInicias = np.float32([[189, 87], [459, 84], [192, 373], [484, 372]])
pontosFinais  = np.float32([[0, 0], [500, 0], [0, 500], [500, 500]])

pontosInicias2 = np.float32([[72, 58], [148, 74], [51, 382], [141, 378]])
pontosFinais2  = np.float32([[0, 0], [166, 0], [0, 500], [166, 500]])

matriz = cv2.getPerspectiveTransform(pontosInicias, pontosFinais)
matriz2 = cv2.getPerspectiveTransform(pontosInicias2, pontosFinais2)

imagemModificada = cv2.warpPerspective(imagemOriginal, matriz, (500, 500))
imagemModificada2 = cv2.warpPerspective(imagemOriginal, matriz2, (166, 500))

cv2.imshow("imagemOriginal", imagemOriginal)
cv2.imshow("imagemModificada", imagemModificada)
cv2.imshow("imagemModificada2", imagemModificada2)

cv2.waitKey(0)
cv2.destroyAllWindows()
