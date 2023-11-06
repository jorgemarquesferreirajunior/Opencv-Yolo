import cv2

capture = cv2.VideoCapture("videos/bigpig.webm")
while True:
    check, frame = capture.read()
    cv2.imshow("USING VIDEOS TO CAPTURE", frame)
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
