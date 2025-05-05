import cv2
import numpy as np

img = cv2.imread('./Imagenes/img_ruido.jpg')

AV_filter = np.array([[1, 1, 1],
                        [1, 1, 1],
                        [1, 1, 1]]) / 9

img_AV = cv2.filter2D(img, -1, AV_filter)
img_AV_cv2 = cv2.blur(img, (5, 5))

cv2.imshow("Imagen con filtro AV", img_AV)
cv2.imshow("Imagen con filtro AV (cv2)", img_AV_cv2)
cv2.imshow("Imagen con ruido", img)

cv2.imwrite('./Imagenes/img_AV.jpg', img_AV)
cv2.imwrite('./Imagenes/img_AV_cv2.jpg', img_AV_cv2)

cv2.waitKey(0)
cv2.destroyAllWindows()
