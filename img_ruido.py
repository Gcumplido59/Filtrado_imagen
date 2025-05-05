import cv2
import numpy as np

imagen = cv2.imread('./Imagenes/ball.jpg')
#Ruido
def add_salt_pepper(imagen, probabilidad):
    noisy_img = imagen.copy()
    #calcula el numero total de pixeles
    num_pixels = imagen.shape[0] * imagen.shape[1]
    #Generar un arreglo de indices de pixeles a modificar
    indices = np.random.choice(num_pixels, size=int(num_pixels * probabilidad), replace=False)
    
    #Iterar sobre los indices y modificar pixeles
    for index in indices:
        # Obtener las coordenadas del píxel
        row = index // imagen.shape[1]  # División entera
        col = index % imagen.shape[1]   # Resto de la división
        
        # Decidir si agregar "sal" o "pimienta" (50% de probabilidad)
        if np.random.rand() < 0.5:
            # Agregar "sal" (blanco)
            noisy_img[row, col] = 255  # o cualquier valor de blanco deseado
        else:
            # Agregar "pimienta" (negro)
            noisy_img[row, col] = 0    # o cualquier valor de negro deseado
            
    return noisy_img

noise_probability = 0.1
noisy_image = add_salt_pepper(imagen, noise_probability)


cv2.imshow("Imagen con ruido sal y pimienta", noisy_image)
cv2.imwrite('./Imagenes/img_ruido.jpg', noisy_image)
cv2.waitKey(0)
cv2.destroyAllWindows()