import cv2

img = cv2.imread('./Imagenes/ball.jpg')

# Factor de submuestreo (por ejemplo, 2 reduce el tamaño a la mitad)
factor = 8

# Submuestreo: tomar 1 de cada 'factor' píxeles
img_achicado= img[::factor, ::factor]


cv2.imshow('Original', img)
cv2.imshow(f'Img Achicado x{factor}', img_achicado)
cv2.imwrite('./Imagenes/img_subs.jpg', img_achicado)
cv2.waitKey(0)
cv2.destroyAllWindows()

