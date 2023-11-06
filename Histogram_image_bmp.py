import cv2
from matplotlib import pyplot as grafico

img_inicial = cv2.imread("images/leaves/leaf_01.bmp", 0)
grafico.hist(img_inicial.ravel(), 256, [0,256])
grafico.show()

#
# image_gray = cv2.cvtColor(img_inicial, cv2.COLOR_BGR2GRAY)
# cv2.imwrite("images/leaves/leaf_01.bmp", image_gray)
#
# image_gray = cv2.imread("images/fruits/various_gray.bmp", 0)
# _, binary_image = cv2.threshold(image_gray, 130, 255, cv2.THRESH_BINARY)
#
# cv2.imwrite("images/fruits/various_binary.bmp", binary_image)
# img = cv2.imread("images/fruits/various_binary.bmp", 0)
#
# tot_black_pixels, tot_white_pixels = 0, 0
# height_img = img.shape[0]
# width_img = img.shape[1]
#
# for h in range(height_img):
#     for w in range(width_img):
#         pixel_value = img[h, w]
#         if pixel_value == 255:
#             tot_white_pixels += 1
#         else:
#             tot_black_pixels += 1
#
# print(f"{'Total pixels brancos:':<22} {tot_white_pixels}")
# print(f"{'Total pixels pretos:':<22} {tot_black_pixels}")
#
# grafico.hist(img.ravel(), 256, [0, 256])
# grafico.show()
# binary_image = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 16)

