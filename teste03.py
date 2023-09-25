import cv2

##abrindo a camera com o OpenCV
webcamera = cv2.VideoCapture(0)
while True:
    camera, frame = webcamera.read()
    cv2.imshow("Imagem Camera", frame)
    if cv2.waitKey(1) == ord('q'):
        break
webcamera.release()
cv2.destroyAllWindows()
