import cv2
from ultralytics import YOLO
import winsound
import threading

# monitorando video

video = cv2.VideoCapture("C:/Users/Mi/Documents/GitHub/Opencv-Yolo/Videos/pessoaCaminhando.mp4")
modelo = YOLO('yolov8n.pt')
# BGR
bgr_blue = (255, 0, 0)
bgr_green = (0, 255, 0)
bgr_red = (0, 0, 255)
bgr_black = (0, 0, 0)
bgr_white = (255, 255, 255)
borda_n1 = -1
borda_1 = 1
borda_3 = 3
borda_5 = 5
raio_5 = 5
area = [15, 300, 210, 350]
pos_1 = (105, 65)
pos_2 = (100, 30)
box_1 = (470, 80)
font_1 = cv2.FONT_HERSHEY_SIMPLEX
font_scale_1 = 1
alarmeCtrl = False

def alarme():

    global alarmeCtrl
    for _ in range(5):
        winsound.Beep(2500, 500)

    alarmeCtrl = False

while True:

    _, img = video.read()
    img2 = img.copy()
    cv2.rectangle(img2, (area[0], area[1]), (area[0] + area[2], area[1] + area[3]), bgr_green, -1)
    resultado = modelo(img)

    for objetos in resultado:
        obj = objetos.boxes
        for dados in obj:
            x, y, w, h = dados.xyxy[0]
            x, y, w, h = int(x), int(y), int(w), int(h)
            cls = int(dados.cls[0])
            cx, cy = (x + w) // 2, (y + h) // 2
            cv2.circle(img, (cx, cy), raio_5, bgr_black, borda_5)
            if cls == 0:
                cv2.rectangle(img, (x, y), (w, h), bgr_blue, borda_1)
                if area[0] <= cx <= area[2] + area[0] and area[1] <= cy <= area[3] + area[1]:
                    # print("Dentro da area")
                    cv2.rectangle(img2, (area[0], area[1]), (area[0] + area[2], area[1] + area[3]), bgr_red, borda_n1)
                    cv2.rectangle(img, pos_2, box_1, bgr_red, borda_n1)
                    cv2.putText(img, "PESSOA DETECTADA", pos_1, font_1, font_scale_1, bgr_white, borda_3)
                    if not alarmeCtrl:
                        alarmeCtrl = True
                        threading.Thread(target=alarme()).start()
    imgFinal = cv2.addWeighted(img2, 0.5, img, 0.5, 0)
    cv2.imshow('Video', imgFinal)
    if cv2.waitKey(1) == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
