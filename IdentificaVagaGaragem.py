import numpy as np
import cv2

vaga1 = [1, 89, 108, 213]
vaga2 = [115, 87, 152, 211]
vaga3 = [289, 89, 138, 212]
vaga4 = [439, 87, 135, 212]
vaga5 = [591, 90, 132, 206]
vaga6 = [738, 93, 139, 204]
vaga7 = [881, 93, 138, 201]
vaga8 = [1027, 94, 147, 202]
vagas = []

for i in range(1, 9):
    nome_vaga = f'vaga{i}'
    lista_vaga = locals()[nome_vaga]
    vagas.append(lista_vaga)
pathAcer  ="C:/Users/Mi/Desktop/video.mp4"
pathDell = "C:/Users/engen/Desktop/Docs/Opencv-all/Arquivos_aula_contador_vagas/video.mp4"
pathVideo = pathAcer
video = cv2.VideoCapture(pathVideo)

while True:
    check, img = video.read()
    imgCinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgTh = cv2.adaptiveThreshold(imgCinza, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    imgBlur = cv2.medianBlur(imgTh, 5)
    kernel = np.ones((3,3), np.int8)
    imgDl = cv2.dilate(imgBlur, kernel)
    qtd_vagas_livres = 0
    for x, y, w, h in vagas:
        recorte_vaga = imgDl[y:y+h, x:x+w]
        qtd_white_pixels = cv2.countNonZero(recorte_vaga)
        cv2.putText(img, str(qtd_white_pixels), (x, y+h-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        if qtd_white_pixels > 3000:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)  # BGR
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)  # BGR
            qtd_vagas_livres += 1
    cv2.rectangle(img, (30, 30), (225, 70), (255, 0, 0), -1)
    cv2.putText(img, f"LIVRE: {qtd_vagas_livres}/8", (30, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow("Video", img)

    cv2.imshow("Video Dl", imgDl)
    if cv2.waitKey(10) == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
