import cv2

# Cargar la imagen en escala de grises
imagen = cv2.imread('/Users/jimmy/Documents/Mac/Escuela/Cuarto/Procesamiento de Imagenes/proyecto/Imagenes/Imagen_original.png', cv2.IMREAD_GRAYSCALE)

# Aplicar umbralado global
umbral = 127
_, imagen_umbralada = cv2.threshold(imagen, umbral, 255, cv2.THRESH_BINARY)


cv2.imshow('Imagen Original', imagen)# imagen original

cv2.imshow('Imagen Umbralada', imagen_umbralada) # imagen umbralada

cv2.waitKey(0) # cerrar las ventanas
cv2.destroyAllWindows()
