import cv2

image = cv2.imread("images/animals/pigs01.jpeg")
while True:
    cv2.imshow("Happy Pigs", image)
    if cv2.waitKey(0) == ord('q'):
        break

cv2.destroyAllWindows()
