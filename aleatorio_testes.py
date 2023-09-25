"""
# copiando dados de um diretorio para outro e alterando nome:

from imutils import paths
import os
import shutil
from PIL import Image
import matplotlib.pyplot as plt
import cv2

imagemPath = list(paths.list_images('C:/Users/Mi/Documents/GitHub/Opencv-Yolo/images'))

if not os.path.exists('neg'):
    os.makedirs('neg')
for v, i in enumerate(imagemPath):
    terminacao = 'neg/' + str(v).zfill(3) + i[-4:]
    im = i.replace(i, terminacao)
    shutil.copy(i, im)

    # redimensionando imagens e alterando escala de cores
    # imGray = cv2.imread(terminacao, cv2.IMREAD_GRAYSCALE)
    # resized_image = cv2.resize(imGray, (100, 100))
    # cv2.imwrite(terminacao, resized_image)

diretorio = 'C:/Users/Mi/Documents/GitHub/Opencv-Yolo/neg'
images = os.listdir(diretorio)
for arq in images:
    if arq.endswith(('.jpg', '.png')):
        imagem = Image.open(os.path.join(diretorio, arq))
        largura, altura = imagem.size
        print(f'Nomedo arquivo {arq}, Largura:{largura}, Altura:{altura}')
        plt.imshow(imagem)
        plt.axis('off')  # Desligue os eixos para evitar números nos cantos
        plt.show()
"""

"""
# removendo diretorios não vazios
import os
import shutil

if os.path.exists('neg'):
    shutil.rmtree('neg') # remove diretorios não vazios

"""

"""
# copiando imagens de uma pasta para outra, renomeanod cada imagem
# e abrindo cada imagem
from imutils import paths
import os
import shutil
from PIL import Image
import matplotlib.pyplot as plt

imagemPath = list(paths.list_images('C:/Users/Mi/Documents/GitHub/Opencv-Yolo/images'))

if not os.path.exists('neg'):
    os.makedirs('neg')
for v, i in enumerate(imagemPath):
    im = i.replace(i, 'neg/' + str(v).zfill(3) + i[-4:])
    shutil.copy(i, im)
diretorio = 'C:/Users/Mi/Documents/GitHub/Opencv-Yolo/neg'
images = os.listdir(diretorio)
for arq in images:
    if arq.endswith(('.jpg', '.png')):
        imagem = Image.open(os.path.join(diretorio, arq))
        largura, altura = imagem.size
        print(f'Nomedo arquivo {arq}, Largura:{largura}, Altura:{altura}')
        plt.imshow(imagem)
        plt.axis('off')  # Desligue os eixos para evitar números nos cantos
        plt.show()
"""


"""
# manipulação de diretórios
import os

if not os.path.exists('neg'):
    # cria um diretorio
    os.makedirs('neg')
else:
    # deleta um diretorio
    os.rmdir('neg')
numero = 1
"""


"""
# formatando numero com zeros a esquerda
numero = 12
print(str(numero).zfill(5))
"""
