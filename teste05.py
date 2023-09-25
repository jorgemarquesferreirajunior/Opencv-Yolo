import cv2

# detectando o olho...
# seleciona a camera: defult = 0
webCamera = cv2.VideoCapture(0)
# seleciona o arquivo de base de dados para comparação
classificadorFace = cv2.CascadeClassifier('C:/Users/Mi/Documents/GitHub/Opencv-Yolo/haarcascades'
                                    '/haarcascade_frontalface_default.xml')
classificadorEye = cv2.CascadeClassifier('C:/Users/Mi/Documents/GitHub/Opencv-Yolo/haarcascades'
                                 '/haarcascade_eye.xml')
# criando algumas variaveis de cores para facilitar o código
colorGray = cv2.COLOR_BGR2GRAY
colorRedRGB = (255, 0, 0)
colorBlueRGB = (0, 0, 255)
colorGreenRGB = (0, 255, 0)
borda01 = 1
# crianto uma repetição para mostrar o que a camera esta visualizando
while True:
    # lendo a informação obtida pela camera
    camera, frame = webCamera.read()
    # dados obtidos pela camera em uma escala de cores cinza
    cameraGray = cv2.cvtColor(frame, colorGray)
    # classifcando o dado da escala de cinza, obtido pela camera
    detected = classificadorFace.detectMultiScale(cameraGray)
    # criando um retangulo em torno do dado detectado
    for x, y, l, a in detected:
        # ponto de ancoragem do retangulo
        pointFace = (x, y)
        # dimensões do retangulo
        dimensionsFace = (x + l, y + a)
        # criando o retangulo da face
        rectFace = cv2.rectangle(frame, pointFace, dimensionsFace, colorRedRGB, borda01)
        # definindo o dimesoes para procura do olho
        find_eye = rectFace[y:y + a, x:x + l]
        # alternando para a escala de cinza
        find_eye_gray = cv2.cvtColor(find_eye, colorGray)
        # detectando o olho
        detected = classificadorEye.detectMultiScale(find_eye_gray)
        for X_eye, Y_eye, W_eye, H_eye in detected:
            # ponto de ancoragem do olho
            pointEye = (X_eye, Y_eye)
            # dimensões do olho
            dimensionsEye = (X_eye + W_eye, Y_eye + H_eye)
            # criando o retangulo do olho
            rectEye = cv2.rectangle(find_eye, pointEye, dimensionsEye, colorGreenRGB, 2)
    # mostrando os dados detectados
    cv2.imshow("Detecta Face", frame)
    # fechando a janela ao pressionar a tecla "c" do teclado
    if cv2.waitKey(1) == ord("c"):
        # break faz com que saimos da repetição
        break
# ao sair da repetição, limpamos a camera e depois fechamos a janela de visualização
webCamera.release()
cv2.destroyAllWindows()
