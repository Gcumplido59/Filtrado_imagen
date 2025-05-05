import cv2
import numpy as np

img = cv2.imread('./Imagenes/img_ruido.jpg')

GAUSSIAN_filter = np.array([[np.power(np.e, -4), np.power(np.e, -3), np.power(np.e, -2)],
                        [np.power(np.e, -3), np.power(np.e, -2), np.power(np.e, -1)],
                        [np.power(np.e, -2), np.power(np.e, -1), np.power(np.e, 0)]]) / (4/np.pi)

img_GAUSSIAN = cv2.filter2D(img, -1, GAUSSIAN_filter)

img_gauss_cv2 = cv2.GaussianBlur(img, (5, 5), 0)


cv2.imshow("Imagen con filtro Gaussiano", img_GAUSSIAN)
cv2.imshow("Imagen con filtro Gaussiano (cv2)", img_gauss_cv2)
cv2.imshow("Imagen sin filtro", img)

cv2.imwrite('./Imagenes/img_GAUSSIAN.jpg', img_GAUSSIAN)
cv2.imwrite('./Imagenes/img_GAUSSIAN_cv2.jpg', img_gauss_cv2)

cv2.waitKey(0)
cv2.destroyAllWindows()
