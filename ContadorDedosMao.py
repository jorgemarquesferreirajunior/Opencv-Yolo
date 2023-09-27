import cv2, mediapipe as mp


ipDell = ""
video = cv2.VideoCapture()
video.open(ipDell)

hand = mp.solutions.hands
Hand = hand.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

