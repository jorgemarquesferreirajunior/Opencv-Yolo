import cv2
import os

cwd = os.getcwd()
paths = os.listdir(cwd)
images_cv2 = []
for path in paths:
    if path == "images":
        images_path = os.path.join(cwd, path)
        images_lis = os.listdir(images_path)
        for image in images_lis:
            images_cv2.append(os.path.join(images_path, image))
path = "C:/Users/engen/Documents/GitHub/Opencv-Yolo/haarcascades/haarcascade_frontalface_default.xml"
push_alg = cv2.CascadeClassifier(path)
fator = 0.5
indice = 1
try:
    imagem = cv2.imread(images_cv2[indice])
    imagem = cv2.resize(imagem, (int(1370 * fator), int(749 * fator)))
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    faces = push_alg.detectMultiScale(imagem_cinza, scaleFactor=1.05, minNeighbors=4, minSize=(100, 100))
    for x, y, w, h in faces:
        cv2.rectangle(imagem, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("Faces", imagem)
    print(cv2.getWindowImageRect("Faces"))
    cv2.waitKey()
except:
    print("Numero errado")

"""
images_cv2_read = []
images_cv2_gray = []
faces = []
for i in images_cv2:
    images_cv2_read.append(cv2.imread(i))
for a in images_cv2_read:
    images_cv2_gray.append(cv2.cvtColor(a, cv2.COLOR_BGR2GRAY))
for j in images_cv2_gray:
    faces.append(push_alg.detectMultiScale(j))
indice = 3
face = faces[indice] #criando a face de manipulacao
for x, y, w, h in face:
    cv2.rectangle(images_cv2_read[indice], (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow("Faces ", images_cv2_read[indice])
cv2.waitKey()
"""
