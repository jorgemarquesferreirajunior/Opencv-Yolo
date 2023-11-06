import cv2
#escala de cores HSV - hue, saturation, value

image = cv2.imread("images/fruits/various.jpg")
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
hue, saturation, value = cv2.split(image_hsv)
image_merge = cv2.merge((hue, saturation, value))
image_merge = cv2.cvtColor(image_merge, cv2.COLOR_HSV2BGR)
while True:
    cv2.imshow("Canal H",hue)
    cv2.imshow("Canal S", saturation)
    cv2.imshow("Canal V", value)
    cv2.imshow('Merge_HSV', image_merge)

    if cv2.waitKey(0) == ord('q'):
        break
cv2.destroyAllWindows()


