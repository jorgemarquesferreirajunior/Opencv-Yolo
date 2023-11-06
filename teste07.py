import cv2
import numpy as np

video = cv2.VideoCapture()
ip = "https://192.168.0.105:8080/video"
video.open(ip)

while True:
    _, frame = video.read()
    #frame = cv2.rotate(frame, cv2.ROTATE_180)
    fator = 0.5
    frame = cv2.resize(frame, (int(1370 * fator), int(749 * fator)))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    kernel = np.ones((5, 5), np.uint8)
    dilation = cv2.erode(threshold, kernel, iterations=1)
    contornos,_ = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for (i, c) in enumerate(contornos):
        (x, y, a, l) = cv2.boundingRect(c)
        area = cv2.contourArea(c)
        cv2.rectangle(frame, (x, y), (x + a, y + l), (0, 255, 0), 2)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
