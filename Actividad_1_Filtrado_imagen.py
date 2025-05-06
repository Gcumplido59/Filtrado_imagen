import cv2
import numpy as np
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'     # Ruta a tesseract.exe

# Cargar imágenes
imagen1 = cv2.imread('./placa_q.jpg')
imagen2 = cv2.imread('./placa_2.jpg')


img_achicado = imagen2[::2, ::2]        # Achicar imagen2

# Aplicar blur gaussiano
imagenblurgaussiano = cv2.GaussianBlur(imagen1, (35, 35), 0)
imagenblurgaussiano2 = cv2.GaussianBlur(img_achicado, (35, 35), 0)


hsv2 = cv2.cvtColor(imagenblurgaussiano2, cv2.COLOR_BGR2HSV)        # Convertir a HSV para Imagen 2

# Rangos HSV definidos manualmente para la Imagen 2
lower_black2 = np.array([0, 0, 186])
upper_black2 = np.array([150, 80, 255])

# Mascara imagen 2
mascara2 = cv2.inRange(hsv2, lower_black2, upper_black2)
num_img2 = cv2.bitwise_and(imagenblurgaussiano2, imagenblurgaussiano2, mask=mascara2)

# OCR
def ocr_proceso(imagen):
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    _, umbral = cv2.threshold(gris, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return umbral

umbral1 = ocr_proceso(imagenblurgaussiano)
umbral2 = ocr_proceso(num_img2)

# Extraer texto con OCR
texto1 = pytesseract.image_to_string(umbral1, config='--psm 6')
texto2 = pytesseract.image_to_string(umbral2, config='--psm 6')

print("Texto detectado en imagen 1:")
print(texto1)

print("\nTexto detectado en imagen 2:")
print(texto2)

# Imagenes procesadas
cv2.imshow('Imagen 1 - OCR', umbral1)
cv2.imshow('Imagen 2 - OCR', umbral2)
cv2.waitKey(0)
cv2.destroyAllWindows()