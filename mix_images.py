import cv2

fichas_vermelhas = cv2.imread("images/games/poker_red_chips.png")
fichas_pretas = cv2.imread("images/games/poker_black_chips.png")

new_image = cv2.addWeighted(fichas_pretas, 0.2, fichas_vermelhas, 1, 0)

cv2.imshow("fichas_vermelhas", fichas_vermelhas)
cv2.imshow("fichas_pretas", fichas_pretas)
cv2.imshow("new_image", new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
