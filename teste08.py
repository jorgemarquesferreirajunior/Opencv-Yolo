import cv2
import numpy as np
import time

# usando camera do celular como webcam
video = cv2.VideoCapture()
ip = "https://10.139.5.214:8080/video"
video.open(ip)
BGR_blue = (255, 0, 0)
BGR_green = (0, 255, 0)
BGR_yellow = (0, 255, 255)
borda1 = 1
borda2 = 2
while True:

    check, img = video.read()
    img = cv2.rotate(img, cv2.ROTATE_180)
    fator = 0.5
    img = cv2.resize(img, (int(1370 * fator), int(749 * fator)))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    kernel = np.ones((5, 5), np.uint8)
    dilation = cv2.erode(threshold, kernel, iterations=1)
    contornos, _ = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for (i, c) in enumerate(contornos):
        (x, y, a, l) = cv2.boundingRect(c)
        area = cv2.contourArea(c)
        mmY = int((l*19.5) / 184)
        mmX = int((l * 17) / 214)
        if mmY > 0:
            cv2.rectangle(img, (x, y), (x + a, y + l), BGR_green, borda2)
            cv2.putText(img, str(mmY)+"mm", (x, y + l + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, BGR_yellow, borda1)
            cv2.putText(img, str(mmX)+"mm", (x + a + 15, y + l + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, BGR_yellow, borda1)

    cv2.imshow("Img", img)
    # print(cv2.getWindowImageRect("Img"))

    if cv2.waitKey(1) == ord('q'):
        break
video.release()
cv2.destroyAllWindows()