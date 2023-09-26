import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import numpy as np

# detectando a mao...

video = cv2.VideoCapture()
ip = "https://10.139.5.214:8080/video"
video.open(ip)
# video.set(3, 1280)
# video.set(4, 720)
detectorMao = HandDetector(detectionCon=0.8, maxHands=2)

distPixels = [300, 245, 200, 170, 145, 130, 112, 103, 93, 87, 80, 75, 70, 67, 62, 59, 57]
distCm = []
for i in range(20, 101, 5):
    distCm.append(i)

coef = np.polyfit(distPixels, distCm, 2)
right_hand = ""
left_hand = ""
while True:
    _, img = video.read()

    img = cv2.rotate(img, cv2.ROTATE_180)
    fator = 0.5
    img = cv2.resize(img, (int(1370 * fator), int(749 * fator)))
    hands = detectorMao.findHands(img, draw=True)# draw=True mostra os pontos das falanges
    # print(hands)
    if len(hands[0]) > 0:
        hand = hands[0][0]['lmList']
        type_hand = hands[0][0]['type']
        try:
            if type_hand == 'Right':
                right_hand = type_hand
            if type_hand == 'Left':
                left_hand = type_hand
        except:
            right_hand = ""
            left_hand = ""
        print(right_hand, left_hand)
        x, y, w, h = hands[0][0]['bbox']
        # print(f"INDEX_FINGER_MCP: {hand[5]}| PINKY_MCP: {hand[17]}")

        x1, y1, _ = hand[5]
        x2, y2, _ = hand[17]
        A, B, C = coef
        distancia = abs(x2 - x1)
        distanciaCM = (A*distancia**2)+(B*distancia) + C
        # print(f"Pixels: {distancia} Centímetros: {int(distanciaCM)}")
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 3)
        #cv2.putText(img, str(int(distanciaCM)), (), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), -1)
        cvzone.putTextRect(img, str(int(distanciaCM))+"cm", (x+5, y-10))

    cv2.imshow("Window", img)
    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
