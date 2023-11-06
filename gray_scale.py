import cv2
#aplicando escala de cinza para uma imagem qualquer
image = cv2.imread("images/fruits/various.bmp")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("images/fruits/various_lab.bmp", image_gray)
while True:
    cv2.imshow("REAL IMAGE", image)
    cv2.imshow("GRAY IMAGE", image_gray)
    if cv2.waitKey(0) == ord('q'):
        break
cv2.destroyAllWindows()
