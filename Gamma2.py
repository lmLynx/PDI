import cv2
import numpy as np

class Gama:
    def aplicar(self, img):
        # Implementar corrección de gama
        gamma = 2.0
        invGamma = 1.0 / gamma
        table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
        img_gama = cv2.LUT(img, table)
        return img_gama
