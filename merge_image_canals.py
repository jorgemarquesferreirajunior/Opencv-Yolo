import cv2
# erverso do split - merge dos tres canais de cores - BGR
image = cv2.imread("images/fruits/various.jpg")
blue, green, red = cv2.split(image)
image_merge = cv2.merge((blue, green, red))

while True:
    cv2.imshow("IMAGE MERGED", image_merge)
    if cv2.waitKey(0) == ord('q'):
        break
cv2.destroyAllWindows()
