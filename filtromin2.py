import cv2
import numpy as np

class FiltroMin:
    def aplicar(self, img):
        # Implementar el filtro mínimo
        kernel = np.ones((5,5),np.uint8)
        img_min = cv2.erode(img, kernel, iterations = 1)
        return img_min
