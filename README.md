# 🔍 OCR de Placas Vehiculares con OpenCV y Tesseract

Este proyecto permite realizar **detección y extracción de texto en placas de vehículos** mediante técnicas de procesamiento de imágenes y reconocimiento óptico de caracteres (OCR). Utiliza `OpenCV` para el filtrado y preprocesamiento de imágenes, y `Tesseract OCR` a través de la biblioteca `pytesseract` para identificar el texto presente.

---

## 📌 Funcionalidades principales

1. **Carga y redimensionamiento de imágenes**:
   - Se procesan dos imágenes (`placa_q.jpg` y `placa_2.jpg`) desde la carpeta `Imagenes/`.
   - La segunda imagen se reduce a la mitad de su tamaño para disminuir el procesamiento.

2. **Filtrado Gaussiano**:
   - Se aplica un desenfoque Gaussiano para reducir ruido y facilitar la detección de texto.

3. **Conversión a HSV y creación de máscaras**:
   - Se realiza una conversión a HSV y se define un rango específico para extraer regiones oscuras donde es probable que se encuentre el texto.

4. **Preprocesamiento para OCR**:
   - Las imágenes se convierten a escala de grises y se binarizan mediante umbralización Otsu.

5. **Extracción de texto**:
   - Se usa `pytesseract` para extraer el texto procesado, utilizando el modo `--psm 6` (una sola línea o bloque de texto).

6. **Visualización**:
   - Se muestran las imágenes binarizadas en pantalla.
   - Se imprime el texto reconocido en la consola.

---

## 🧪 Requisitos del sistema

- Python 3.7 o superior
- Sistema operativo Windows (aunque puede adaptarse a Linux/Mac)
- Tesseract OCR instalado y accesible

---

## 🧰 Instalación de dependencias

### 1. Instalar Python y `pip`
Asegúrate de tener Python instalado. Puedes descargarlo desde:  
📦 https://www.python.org/downloads/

Verifica las instalaciónes:
```bash
python --version
pip --version
```
### 2. Instalar librerias
desde la terminal ejecutar:
```bash
pip install opencv-python
pip install numpy
pip install pytesseract
```




