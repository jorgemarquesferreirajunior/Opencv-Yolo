import cv2

fichas_vermelhas = cv2.imread("images/games/poker_red_chips.png")
fichas_pretas = cv2.imread("images/games/poker_black_chips.png")

imagem_add = cv2.add(fichas_pretas, fichas_vermelhas)

cv2.imshow("fichas_vermelhas", fichas_vermelhas)
cv2.imshow("fichas_pretas", fichas_pretas)
cv2.imshow("imagem_add", imagem_add)
cv2.waitKey(0)
cv2.destroyAllWindows()
