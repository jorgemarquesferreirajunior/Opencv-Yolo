import cv2
from matplotlib import pyplot as grafico

imagem_original = cv2.imread("images/objects/clock.png", 0)
imagem_equalizada = cv2.equalizeHist(imagem_original)

cv2.imshow("imagem Original", imagem_original)
cv2.imshow("imagem equalizada", imagem_equalizada)

grafico.hist(imagem_original.ravel(), 256, [0, 256])
grafico.figure()
grafico.hist(imagem_equalizada.ravel(), 256,  [0, 256])
grafico.show()

cv2.destroyAllWindows()
# while True:
#     cv2.imshow("imagem Original", imagem_original)
#     cv2.imshow("imagem equalizada", imagem_equalizada)
#     # plot..
#
#
#     if cv2.waitKey(0) == ord('q'):
#       break

#