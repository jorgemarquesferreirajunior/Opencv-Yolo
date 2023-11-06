from ultralytics import YOLO

model = YOLO("yolov8n.yaml")

results = model.train(data="coco128.yaml", epochs=3)

results = model.val()
results = model("")
success = model.export(format="onnx")













# import cv2
#
# carrega_algoritmo = cv2.CascadeClassifier('C:/Users/Mi/Documents/GitHub/Opencv-Yolo/haarcascades'
#                                           '/haarcascade_frontalface_default.xml')
# imagem = cv2.imread('C:/Users/Mi/Documents/GitHub/Opencv-Yolo/images/image07.jpg')
# imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
# faces = carrega_algoritmo.detectMultiScale(imagemCinza)
#
# print(faces)
# for(x, y, w, h) in faces:
#     cv2.rectangle(imagem, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
# cv2.imshow('Faces', imagem)
# cv2.waitKey()
