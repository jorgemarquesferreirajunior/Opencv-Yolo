import cv2

# seleciona a camera: defult = 0
webCamera = cv2.VideoCapture(0)
# seleciona o arquivo de base de dados para comparação
classificador = cv2.CascadeClassifier('C:/Users/Mi/Documents/GitHub/Opencv-Yolo/haarcascades'
                                    '/haarcascade_frontalface_default.xml')
# criando algumas variaveis para facilitar o código
colorGray = cv2.COLOR_BGR2GRAY
colorRedRGB = (255, 0, 0)
# crianto uma repetição para mostrar o que a camera esta visualizando
while True:
    # lendo a informação obtida pela camera
    camera, frame = webCamera.read()
    # dados obtidos pela camera em uma escala de cores cinza
    cameraGray = cv2.cvtColor(frame, colorGray)
    # classifcando o dado da escala de cinza, obtido pela camera
    detected = classificador.detectMultiScale(cameraGray)
    # criando um retangulo em torno do dado detectado
    for x, y, l, a in detected:
        # ponto de ancoragem do retangulo
        point = (x, y)
        # dimensões do retangulo
        dimensions = (x + l, y + a)
        # criando o retangulo
        cv2.rectangle(frame, point, dimensions, colorRedRGB, 2)
    # mostrando o retangulo
    cv2.imshow("Detecta Face", frame)
    # fechando a janela ao pressionar a tecla "c" do teclado
    if cv2.waitKey(1) == ord("c"):
        # break faz com que saimos da repetição
        break
# ao sair da repetição, limpamos a camera e depois fechamos a janela de visualização
webCamera.release()
cv2.destroyAllWindows()
