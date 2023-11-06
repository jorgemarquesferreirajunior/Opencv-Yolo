import cv2
# obtendod n° de linhas, colunas e canais

image = cv2.imread("images/animals/pigs01.jpeg")
shape_img = image.shape
print(f"Altura: {int(shape_img[0])} pixels\nlargura: {int(shape_img[1])} pixels\nN° de canais: {str(shape_img[2]).zfill(2)}")

