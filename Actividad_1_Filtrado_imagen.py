import cv2
import numpy as np
import pytesseract

# Ruta al ejecutable de Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Cargar imágenes de las placas con OpenCV
imagen1 = cv2.imread('./Imagenes/placa_q.jpg')
imagen2 = cv2.imread('./Imagenes/placa_2.jpg')

# Reducir la imagen 2 a la mitad de su tamaño
img_achicado = imagen2[::2, ::2]

# Aplicar filtro Gaussiano para reducir el ruido
imagenblurgaussiano = cv2.GaussianBlur(imagen1, (35, 35), 0)
imagenblurgaussiano2 = cv2.GaussianBlur(img_achicado, (35, 35), 0)

# Convertir la imagen 2 al espacio de color HSV
hsv2 = cv2.cvtColor(imagenblurgaussiano2, cv2.COLOR_BGR2HSV)

# Definir los rangos HSV para detectar texto oscuro en la imagen 2
lower_black2 = np.array([0, 0, 186])
upper_black2 = np.array([150, 80, 255])

# Crear máscara binaria para aislar áreas con texto
mascara2 = cv2.inRange(hsv2, lower_black2, upper_black2)
num_img2 = cv2.bitwise_and(imagenblurgaussiano2, imagenblurgaussiano2, mask=mascara2)

# Función de preprocesamiento de imágenes para OCR
def ocr_proceso(imagen):
    # Convertir a escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Aplicar umbralización Otsu para binarizar la imagen
    _, umbral = cv2.threshold(gris, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return umbral

# Procesar ambas imágenes antes de aplicar OCR
umbral1 = ocr_proceso(imagenblurgaussiano)
umbral2 = ocr_proceso(num_img2)

# Extraer texto usando pytesseract con el modo de segmentación PSM 6
texto1 = pytesseract.image_to_string(umbral1, config='--psm 6')
texto2 = pytesseract.image_to_string(umbral2, config='--psm 6')

# Imprimir los textos extraídos desde ambas imágenes
print("Texto detectado en imagen 1:")
print(texto1)

print("\nTexto detectado en imagen 2:")
print(texto2)

# Mostrar las imágenes procesadas
cv2.imshow('Imagen 1 - OCR', umbral1)
cv2.imshow('Imagen 2 - OCR', umbral2)
cv2.waitKey(0)
cv2.destroyAllWindows()
