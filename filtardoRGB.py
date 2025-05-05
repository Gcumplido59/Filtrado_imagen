import cv2
import numpy as np

# Cargar imagen
img = cv2.imread('./ball.jpg')

# Definir el rango de colores amarillos en RGB
# Nota: OpenCV carga en BGR, así que hay que tener en cuenta eso
# Amarillo en BGR ≈ (0, 255, 255)
lower_yellow = np.array([0, 200, 200])   # BGR
upper_yellow = np.array([100, 255, 255]) # BGR

# Crear máscara para el color amarillo
mask = cv2.inRange(img, lower_yellow, upper_yellow)

# Aplicar la máscara a la imagen filtrada
yellow_only = cv2.bitwise_and(img, img, mask=mask)

# Mostrar y guardar la imagen
cv2.imshow('Solo Amarillos (RGB)', yellow_only)
cv2.imwrite('./solo_amarillos_rgb.jpg', yellow_only)
cv2.waitKey(0)
cv2.destroyAllWindows()
