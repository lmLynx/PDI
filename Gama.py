import cv2
import numpy as np

# Leer la imagen
imagen = cv2.imread('imagen.jpg')

# Verificar si la imagen se cargó correctamente
if imagen is None:
    print("Error: No se pudo cargar la imagen.")
else:
    # Convertir la imagen a escala de grises
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Calcular el histograma de la imagen
    histograma = cv2.calcHist([imagen_gris], [0], None, [256], [0, 256])

    # Normalizar el histograma
    histograma_normalizado = histograma / histograma.sum()

    # Calcular la curva de corrección gamma
    gamma = 1.5  # Ajustar el valor de gamma según sea necesario
    curva_gamma = np.array([((i / 255.0) ** gamma) * 255 for i in range(256)], dtype=np.uint8)

    # Aplicar la corrección gamma a la imagen
    imagen_corregida = cv2.LUT(imagen_gris, curva_gamma)

    # Mostrar las imágenes originales y corregida
    cv2.imshow('Imagen original', imagen_gris)
    cv2.imshow('Imagen corregida', imagen_corregida)

    cv2.waitKey(0)
    cv2.destroyAllWindows()