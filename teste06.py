import numpy as np
import cv2
import time

# detecção de objetos com Yolo...
# Necessário para criar arquivo csv contendo os objetos
from csv import DictWriter
# Definindo a camera de captura
camera = cv2.VideoCapture()
ip = "https://192.168.0.105:8080/video"
camera.open(ip)
# Altura e largura
h, w = None, None
# Carregando csv com nome dos objetos treinados para identificar
with open('yoloDados/YoloNames.names') as f:
    # Lista com todos os nomes
    labels = [line.strip() for line in f]
# Carregando arquivos treinados pelo framework
network = cv2.dnn.readNetFromDarknet('yoloDados/yolov3.cfg', 'yoloDados/yolov3.weights')
# Captura uma lista com todos os nomes treinados pelo framework
layers_names_all = network.getLayerNames()

# Obtendo apenas os nomes de camadas  de saída que precisamos do algoritmo yolov3
# com função  que retorna índices de camadas com saídas desconectadas
layers_names_output = [layers_names_all[i[0] - 1] for i in network.getUnconnectedOutLayers()]
# definindo problabilidade mínima
probability_minimum = 0.5
# definir limite para filtrar caixas delimitadoras fracas
# com supressão não máxima
thershold = 0.3
# gerando cores nas caixas delimitadoras
colours = np.random.randint(0, 255, size=(len(labels), 3), dtype='uint8')
# lood de captura
with open('result.csv', 'w') as arquivo:
    cabecalho = ['Detectado', 'Acuracia']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    while True:
        # captura a camera frame por frame:
        frame = camera.read()

        if w is None or h is None:
            # fatiar apenas dois primeiros elementos da tupla
            h, w = frame.shape[:2]



