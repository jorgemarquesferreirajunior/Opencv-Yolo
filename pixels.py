import cv2
# obtendo os valores das cores RGB de um determinado pixel
image = cv2.imread("images/animals/pigs01.jpeg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(image[150, 150], "\nblue:", end="")
print(image[150, 150, 0], "\ngreen:", end="")
print(image[150, 150, 1], "\nred:", end="")
print(image[150, 150, 2])
print(image_gray[150, 150])
