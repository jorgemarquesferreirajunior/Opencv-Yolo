import os
import cv2

cwd = os.getcwd()
paths = os.listdir(cwd)
images_cv2 = []
for path in paths:
    if path == "images":
        images_path = os.path.join(cwd, path)
        images_lis = os.listdir(images_path)
        for image in images_lis:
            images_cv2.append(os.path.join(images_path, image))
pathAcer = ""
pathDell = "C:/Users/engen/Documents/GitHub/Opencv-Yolo/haarcascades/haarcascade_frontalface_default.xml"
path_eyeAcer = ""
path_eyeDell = "C:/Users/engen/Documents/GitHub/Opencv-Yolo/haarcascades/haarcascade_eye.xml"
push_face = cv2.CascadeClassifier(pathDell)
push_eye = cv2.CascadeClassifier(path_eyeDell)
indice = 5
gray = cv2.COLOR_BGR2GRAY
color1 = (0, 255, 0)
color2 = (0, 0, 255)
try:
    imagem = cv2.imread(images_cv2[indice])
    imagem_cinza = cv2.cvtColor(imagem, gray)
    faces = push_face.detectMultiScale(imagem_cinza, scaleFactor=1.05, minNeighbors=4, minSize=(20, 20))
    for x, y, w, h in faces:
        leitura = cv2.rectangle(imagem, (x, y), (x + w, y + h), color1, 2)
        find_eye = leitura[y:y + h, x:x + w]
        find_eye_gray = cv2.cvtColor(find_eye, gray)
        detected = push_eye.detectMultiScale(find_eye_gray)

        for X_eye, Y_eye, W_eye, H_eye in detected:
            cv2.rectangle(find_eye, (X_eye, Y_eye), (X_eye + W_eye, Y_eye + H_eye), color2, 2)

    cv2.imshow("Faces+Olhos ", imagem)
    cv2.waitKey()
except:
    print("Numero errado")
