import cv2
import numpy as np

# Definir las máscaras de Robinson
kernels = {
    'N': np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]),
    'NE': np.array([[0, 1, 2], [-1, 0, 1], [-2, -1, 0]]),
    'E': np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]]),
    'SE': np.array([[2, 1, 0], [1, 0, -1], [0, -1, -2]]),
    'S': np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]]),
    'SW': np.array([[0, -1, -2], [1, 0, -1], [2, 1, 0]]),
    'W': np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]]),
    'NW': np.array([[-2, -1, 0], [-1, 0, 1], [0, 1, 2]])
}

# Leer la imagen en escala de grises
imagen = cv2.imread('imagen.jpg', cv2.IMREAD_GRAYSCALE)

# Verificar si la imagen se cargó correctamente
if imagen is None:
    print("Error: No se pudo cargar la imagen.")
else:
    # Inicializar la imagen de salida con ceros
    resultado = np.zeros_like(imagen, dtype=np.float32)

    # Aplicar cada una de las máscaras y mantener el valor máximo
    for direction, kernel in kernels.items():
        convolucion = cv2.filter2D(imagen, cv2.CV_32F, kernel)
        resultado = np.maximum(resultado, convolucion)

    # Convertir el resultado a tipo de dato uint8
    resultado = np.uint8(np.clip(resultado, 0, 255))

    # Mostrar las imágenes original y filtrada
    cv2.imshow('Imagen original', imagen)
    cv2.imshow('Imagen filtrada', resultado)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
