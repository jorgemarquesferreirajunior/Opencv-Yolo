import cv2


webcamera = cv2.VideoCapture(0)
webcamera.open(ip)
while True:
    # camera, frame = webcamera.read()
    _, frame = webcamera.read()
    cv2.imshow("Imagem Camera", frame)
    if cv2.waitKey(1) == ord('q'):
        break
webcamera.release()
cv2.destroyAllWindows()
