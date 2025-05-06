import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'     # Ruta a tesseract.exe

# Cargar imagenes de las placas con la libreria OpenCV
imagen1 = cv2.imread('./Imagenes/placa_q.jpg')
imagen2 = cv2.imread('./Imagenes/placa_2.jpg')

img_achicado = imagen2[::2, ::2]        # Se achica la imagen 2 a la mitad de su tamaño

# Aplicacion de filtro gaussiano a la imagen 1 e imagen 2
imagenblurgaussiano = cv2.GaussianBlur(imagen1, (35, 35), 0)
imagenblurgaussiano2 = cv2.GaussianBlur(img_achicado, (35, 35), 0)

hsv2 = cv2.cvtColor(imagenblurgaussiano2, cv2.COLOR_BGR2HSV)        # Convertir a HSV para Imagen 2

# Rangos HSV definidos manualmente para la Imagen 2
lower_black2 = np.array([0, 0, 186])
upper_black2 = np.array([150, 80, 255])

# Se crea mascara para la imagen 2
mascara2 = cv2.inRange(hsv2, lower_black2, upper_black2)
num_img2 = cv2.bitwise_and(imagenblurgaussiano2, imagenblurgaussiano2, mask=mascara2)

# OCR (Reconocimiento de caracteres) para la imagen 1 y la imagen 2
# Se define la funcion de procesamiento de imagenes para OCR
def ocr_proceso(imagen):
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    _, umbral = cv2.threshold(gris, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return umbral

# Procesar imagenes para OCR
umbral1 = ocr_proceso(imagenblurgaussiano)
umbral2 = ocr_proceso(num_img2)

# Extraer texto con OCR y la libreria pytesseract
# Se utiliza el modo de segmentacion 6 (PSM 6) para una sola columna de texto
texto1 = pytesseract.image_to_string(umbral1, config='--psm 6')
texto2 = pytesseract.image_to_string(umbral2, config='--psm 6')

# Mostrar resultados en consola de texto extraido de la imagen 1 y 2
print("Texto detectado en imagen 1:")
print(texto1)
print("\nTexto detectado en imagen 2:")
print(texto2)

# Imagenes procesadas mostradas en ventana
cv2.imshow('Imagen 1 - OCR', umbral1)
cv2.imshow('Imagen 2 - OCR', umbral2)
cv2.waitKey(0)
cv2.destroyAllWindows()