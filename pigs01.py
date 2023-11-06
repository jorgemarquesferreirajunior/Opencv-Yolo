import numpy as np
import cv2

# Carregar a imagem
image_path = 'images/animals/pigs01.jpeg'
image = cv2.imread(image_path)

# Altura e largura da imagem
h, w, _ = image.shape

# Carregando o arquivo com nomes dos objetos treinados para identificar
with open('yoloDados/YoloNames.names') as f:
    # Lista com todos os nomes
    labels = [line.strip() for line in f]

# Carregando arquivos treinados pelo framework YOLO
network = cv2.dnn.readNetFromDarknet('yoloDados/yolov3.cfg', 'yoloDados/yolov3.weights')

# Captura uma lista com todos os nomes das camadas de saída
layers_names_all = network.getLayerNames()

# Obtendo apenas os nomes das camadas de saída que precisamos do algoritmo YOLOv3
layers_names_output = [layers_names_all[i[0] - 1] for i in network.getUnconnectedOutLayers()]

# Definindo probabilidade mínima
probability_minimum = 0.5

# Definindo limite para filtrar caixas delimitadoras fracas com supressão não máxima
threshold = 0.3

# Loop de detecção
results = []  # Armazenar os resultados de detecção

# Passo de detecção
blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
network.setInput(blob)
output_from_network = network.forward(layers_names_output)

# Loop pelas camadas de saída
for output in output_from_network:
    for detection in output:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]

        if confidence > probability_minimum:
            center_x = int(detection[0] * w)
            center_y = int(detection[1] * h)
            width = int(detection[2] * w)
            height = int(detection[3] * h)
            left = int(center_x - width / 2)
            top = int(center_y - height / 2)

            # Armazene as informações da detecção
            results.append({
                "label": labels[class_id],
                "confidence": float(confidence),
                "bbox": (left, top, width, height)
            })

# Agora, você pode processar os resultados, por exemplo, filtrando por porcos
for result in results:
    if result["label"] == "pig" and result["confidence"] > threshold:
        print(f"Animal identificado: {result['label']} (Confiança: {result['confidence']:.2f})")