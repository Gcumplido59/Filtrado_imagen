import cv2
import numpy as np

# Cargar imagen
img = cv2.imread('./Imagenes/ball.jpg')

# Convertir a espacio HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Definir los rangos para el color amarillo en HSV
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])

# Crear una máscara que solo conserve los pixeles amarillos
mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

# Aplicar la máscara a la imagen original
yellow_only = cv2.bitwise_and(img, img, mask=mask)

# Mostrar y guardar la imagen
cv2.imshow('Solo Amarillos', yellow_only)
cv2.imwrite('./Imagenes/solo_amarillos_hsv.jpg', yellow_only)
cv2.waitKey(0)
cv2.destroyAllWindows()
