import cv2

img_org = cv2.imread("images/places/parking.png")
moon = cv2.imread("images/planets/moon.png")

img_laplacian = cv2.Laplacian(img_org, cv2.CV_8U)
img_bilateral_filter = cv2.bilateralFilter(img_org, 9, 75, 75)

img_laplacian2 = cv2.Laplacian(img_bilateral_filter, cv2.CV_8U)
img_subtract = cv2.subtract(img_org, img_laplacian)
img_medianB = cv2.medianBlur(img_subtract,1)

moon_lap = cv2.Laplacian(moon, cv2.CV_8U)
moon_realce = cv2.subtract(moon, moon_lap)

# cv2.imshow("Original", img_org)
# cv2.imshow("Realced", img_subtract)
# cv2.imshow("Laplacian", img_laplacian)
# cv2.imshow("Laplacian + bilateralFilter", img_laplacian2)
# cv2.imshow("Bilateral", img_bilateral_filter)
#
# cv2.imshow("Moon", moon)
# cv2.imshow("Moon-Realced", moon_realce)
# cv2.imshow("MedianBlur", img_medianB)
# cv2.imshow("subtract", img_subtract)


cv2.waitKey(0)
cv2.destroyAllWindows()
