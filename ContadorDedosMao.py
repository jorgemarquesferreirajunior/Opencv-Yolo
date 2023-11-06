import mediapipe as mp
import cv2
import threading
import time

ipDell = ""

video = cv2.VideoCapture()
ip = "https://192.168.0.105:8080/video"
video.open(ip)
# video.open(ipDell)

hand = mp.solutions.hands
Hand = hand.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils


# def print_points():
#     cont = 0
#     while True:
#         if hand_points is not None:
#             for p in hand_points:
#                 print(p)
#                 cont += 1
#                 print(f"contagem: {cont}")
#         time.sleep(1)


def print_contador(img):
    global contador
    while True:
        cv2.putText(img, str(contador), (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 3)
        # print(f"Contagem de dedos: {contador}")
        time.sleep(1)


# hand_points = None
# thread = threading.Thread(target=print_points)
# thread.daemon = True
# thread.start()

contador = 0
while True:
    _, img = video.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Hand.process(imgRGB)
    hand_points = results.multi_hand_landmarks
    h, w, _ = img.shape # dimensoes da imagem
    pontos = []

    thread1 = threading.Thread(target=print_contador, args=(img,))
    thread1.daemon = True
    thread1.start()

    if hand_points:
        for points in hand_points:
            mpDraw.draw_landmarks(img, points, hand.HAND_CONNECTIONS)
            for enum_points, coordenates in enumerate(points.landmark):
                # print(enum_points, coordenates)
                cx, cy = int(coordenates.x*w), int(coordenates.y*h)
                cv2.putText(img, str(enum_points), (cx, cy+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                # indicador 8-5 , medio 12-9, anelar 16-13, minimo 20-17
                pontos.append((cx, cy))
        dedos = [8, 12, 16, 20]
        polegar = pontos[4][0]
        medio = pontos[13][0]
        contador = 0
        if points:
            for x in dedos:
                if pontos[x][1] < pontos[x-2][1]:
                    contador += 1
            if abs(polegar - medio) > 140:
                contador += 1

    cv2.imshow("Hand Capture", img)
    if cv2.waitKey(1) == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
