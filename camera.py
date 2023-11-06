import cv2

detector_face = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")

video = cv2.VideoCapture(0)


def drawRectFace(image, deteccoes, color=0):
    cores = [(0, 0, 255), (0, 255, 255), (255, 0, 255), (255, 255, 255)]
    for x, y, h, w in deteccoes:
        print(h, w)
        cv2.rectangle(image, (x, y), (x + h, y + w), cores[color])


def swap(video):
    video.release()
    cv2.destroyAllWindows()


while True:
    check, frame = video.read()

    frame_cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    deteccoes = detector_face.detectMultiScale(frame_cinza, scaleFactor=1.1, minNeighbors=3, minSize=(120, 120), maxSize=(200, 200))

    drawRectFace(frame, deteccoes)

    cv2.imshow('tela', frame)

    if cv2.waitKey(1) == ord('q'):
        break

swap(video)
