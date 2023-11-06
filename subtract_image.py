import cv2

ficha_pos1 = cv2.imread("images/games/poker_chips_pos1.png")
ficha_pos2 = cv2.imread("images/games/poker_chips_pos2.png")


ficha_minus = cv2.subtract(ficha_pos2, ficha_pos1)

cv2.imshow("ficha_pos1", ficha_pos1)
cv2.imshow("ficha_pos2", ficha_pos2)
cv2.imshow("ficha_minus", ficha_minus)


cv2.waitKey(0)
cv2.destroyAllWindows()
