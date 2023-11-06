import cv2
import numpy as np
# diferentes escalas de cores de uma uma imagem

image = cv2.imread("images/fruits/various.jpg")
blue_img, green_img, red_img = cv2.split(image)

while True:
    blue_colored = cv2.merge([blue_img, np.zeros_like(green_img), np.zeros_like(red_img)])
    green_colored = cv2.merge([np.zeros_like(blue_img), green_img, np.zeros_like(red_img)])
    red_colored = cv2.merge([np.zeros_like(blue_img), np.zeros_like(green_img), red_img])

    cv2.imshow("BLUE MATRIX", blue_img)
    cv2.imshow("GREEN MATRIX", green_img)
    cv2.imshow("RED MATRIX", red_img)
    cv2.imshow("BLUE IMAGE", blue_colored)
    cv2.imshow("GREEN IMAGE", green_colored)
    cv2.imshow("RED IMAGE", red_colored)

    if cv2.waitKey(0) == ord('q'):
        break

cv2.imwrite("images/fruits/various_blue_matrix.jpg", blue_img)
cv2.imwrite("images/fruits/various_green_matrix.jpg", green_img)
cv2.imwrite("images/fruits/various_red_matrix.jpg", red_img)
cv2.imwrite("images/fruits/various_blue_colored.jpg", blue_colored)
cv2.imwrite("images/fruits/various_green_colored.jpg", green_colored)
cv2.imwrite("images/fruits/various_red_colored.jpg", red_colored)

cv2.destroyAllWindows()
