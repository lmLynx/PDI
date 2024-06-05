import cv2
import numpy as np

class FiltroRobinson:
    def aplicar(self, img):
        # Implementar el filtro de Robinson
        kernelx = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
        kernely = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
        img_robinson_x = cv2.filter2D(img, -1, kernelx)
        img_robinson_y = cv2.filter2D(img, -1, kernely)
        img_robinson = cv2.addWeighted(img_robinson_x, 0.5, img_robinson_y, 0.5, 0)
        return img_robinson