import cv2
import locale
# obtendod n° de pixels da imagem

image = cv2.imread("images/animals/pigs01.jpeg")
shape_img = image.shape
size_img = image.size / shape_img[2] # como a imagem tem 3 canais
                                    # para encontrar o numero de pixels a conta deve ser:
                                    # (n°linhas X n°colunas) / n°canais
                                    # o metodo size faz o calculo de (n°linhas X n°colunas)

locale.setlocale(locale.LC_ALL, 'pt_BR.utf-8')
size_formatado = locale.format_string("%d", size_img, grouping=True)

print(f"Total de pixels: {size_formatado}")

