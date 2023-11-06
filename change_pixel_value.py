import cv2
# alterando os valores das cores RGB de um determinado pixel
image = cv2.imread("images/animals/pigs01.jpeg")
cores_originais = image[150, 150]
cores_novas = [255, 255, 255]
print("cores originais: ", cores_originais)
image[150, 150] = cores_novas
print("cores originais: ", image[150, 150])
