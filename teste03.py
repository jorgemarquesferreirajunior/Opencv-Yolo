import cv2

##abrindo a camera com o OpenCV
webcamera = cv2.VideoCapture()
ip = "https://192.168.0.105:8080/webcamera"
webcamera.open(ip)
while True:
    # camera, frame = webcamera.read()
    _, frame = webcamera.read()
    cv2.imshow("Imagem Camera", frame)
    if cv2.waitKey(1) == ord('q'):
        break
webcamera.release()
cv2.destroyAllWindows()
