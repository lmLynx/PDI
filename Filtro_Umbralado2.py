import cv2

class FiltroUmbralado:
    def aplicar(self, img):
        # Implementar el filtro umbralado
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, img_umbralado = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        return img_umbralado