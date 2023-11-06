import cv2
from matplotlib import pyplot as grath

containers = cv2.imread("images/objects/containers.png", 0)
containers_ligth = cv2.add(containers, 40)
containers_dark = cv2.add(containers, -40)

cv2.imshow("containers", containers)
cv2.imshow("containers_ligth", containers_ligth)
cv2.imshow("containers_dark", containers_dark)

grath.hist(containers.ravel(), 256, [0, 256])
grath.figure()
grath.hist(containers_ligth.ravel(), 256, [0, 256])
grath.figure()
grath.hist(containers_dark.ravel(), 256, [0, 256])

grath.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
