import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

def ajustar_brillo_contraste(imagen, brillo=0, contraste=0):
        if brillo != 0:
            if brillo > 0:
                shadow = brillo
                max = 255
            else:
                shadow = 0
                max = 255 + brillo
            alpha_b = (max - shadow) / 255
            gamma_b = shadow

            buf = cv2.addWeighted(imagen, alpha_b, imagen, 0, gamma_b)
        else:
            buf = imagen.copy()

        if contraste != 0:
            f = 131 * (contraste + 127) / (127 * (131 - contraste))
            alpha_c = f
            gamma_c = 127 * (1 - f)

            buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)

        return buf
    
def convertir_escala_grises():
    if imagen is not None:
        gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        mostrar_imagen_cv(gris, panel_ajustado)

def suavizar_imagen():
    if imagen is not None:
        valor = suavizar_slider.get()
        suavizada = cv2.GaussianBlur(imagen, (valor, valor), 0)
        mostrar_imagen_cv(suavizada, panel_ajustado)
        
def aplicar_filtro_bilateral():
    if imagen is not None:
        valor = bilateral_slider.get()
        filtrada = cv2.bilateralFilter(imagen, valor, 75, 75)
        mostrar_imagen_cv(filtrada, panel_ajustado,width= 200,height=200)
        
def aplicar_apertura():
    if imagen is not None:
        kernel_size = apertura_slider.get()
        if kernel_size % 2 == 0:
            kernel_size += 1
        imagen_apertura = realizar_apertura(imagen, kernel_size)
        mostrar_imagen_cv(imagen_apertura, panel_ajustado,width= 200,height=200)

def detectar_bordes():
    if imagen is not None:
        valor = bordes_slider.get()
        bordes = cv2.Canny(imagen, valor, valor * 2)
        mostrar_imagen_cv(bordes, panel_ajustado)

def aplicar_ajuste():
    if imagen is not None:
        brillo, contraste = calcular_ajuste_adecuado(imagen)
        actualizar_brillo_contraste_labels(brillo, contraste)
        imagen_ajustada = ajustar_brillo_contraste(imagen, brillo, contraste)
        mostrar_imagen_cv(imagen_ajustada, panel_ajustado, width=200, height=200)

def calcular_ajuste_adecuado(imagen):
    mean_intensity = np.mean(imagen)
    target_intensity = 127
    brillo = target_intensity - mean_intensity
    contraste = 1.5

    return brillo, contraste

def actualizar_brillo_contraste_labels(brillo, contraste):
    brillo_label.config(text=f"Brillo: {brillo}")
    contraste_label.config(text=f"Contraste: {contraste}")


def ajuste_histograma_adaptativo(imagen):
    # Convertir la imagen a escala de grises si no lo está
    if len(imagen.shape) == 3:
        imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    else:
        imagen_gris = imagen.copy()

    # Aplicar el ajuste de histograma adaptativo CLAHE
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    imagen_clahe = clahe.apply(imagen_gris)

    # Fusionar la imagen ajustada en escala de grises con los canales de color originales
    if len(imagen.shape) == 3:
        imagen_ajustada = cv2.merge([imagen_clahe] * 3)
    else:
        imagen_ajustada = imagen_clahe

    return imagen_ajustada
        
def aplicar_grises():
    if imagen is not None:
        gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        mostrar_imagen_cv(gris, panel_ajustado,width= 200,height=200)
        
def aplicar_suavizado():
    if imagen is not None:
        valor = suavizar_slider.get()
        if valor % 2 == 0:
            valor += 1
        suavizada = cv2.GaussianBlur(imagen, (valor, valor), 0)
        mostrar_imagen_cv(suavizada, panel_ajustado,width= 200,height=200)

def aplicar_cierre():
    if imagen is not None:
        kernel_size = cierre_slider.get()
        if kernel_size % 2 == 0:
            kernel_size += 1
        imagen_cierre = realizar_cierre(imagen, kernel_size)
        mostrar_imagen_cv(imagen_cierre, panel_ajustado,width= 200,height=200)

def aplicar_erosion():
    if imagen is not None:
        kernel_size = erosion_slider.get()
        if kernel_size % 2 == 0:
            kernel_size += 1
        imagen_erosionada = realizar_erosion(imagen, kernel_size)
        mostrar_imagen_cv(imagen_erosionada, panel_ajustado,width= 200,height=200)

def aplicar_dilatacion():
    if imagen is not None:
        kernel_size = dilatacion_slider.get()
        if kernel_size % 2 == 0:
            kernel_size += 1
        imagen_dilatada = realizar_dilatacion(imagen, kernel_size)
        mostrar_imagen_cv(imagen_dilatada, panel_ajustado,width= 200,height=200)

def realizar_apertura(imagen, kernel_size):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    apertura = cv2.morphologyEx(imagen, cv2.MORPH_OPEN, kernel)
    return apertura

def realizar_cierre(imagen, kernel_size):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    cierre = cv2.morphologyEx(imagen, cv2.MORPH_CLOSE, kernel)
    return cierre

def realizar_dilatacion(imagen, kernel_size):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    dilatada = cv2.dilate(imagen, kernel, iterations=1)
    return dilatada

def realizar_erosion(imagen, kernel_size):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    erosionada = cv2.erode(imagen, kernel, iterations=1)
    return erosionada

def cargar_imagen():
    global imagen, imagen_path
    imagen_path = filedialog.askopenfilename()
    if imagen_path:
        imagen = cv2.imread(imagen_path, cv2.IMREAD_COLOR)
        mostrar_imagen_cv(imagen, panel_original,width= 200,height=200)
        
        
def actualizar_brillo_contraste(val):
    brillo = brillo_slider.get()
    contraste = contraste_slider.get()
    imagen_ajustada = ajustar_brillo_contraste(imagen, brillo, contraste)
    mostrar_imagen_cv(imagen_ajustada, panel_ajustado,width= 200,height=200)


def mostrar_imagen_cv(imagen, panel, width=None, height=None):
    if width and height:
        imagen = cv2.resize(imagen, (width, height))

    borde_size = 5
    imagen = cv2.copyMakeBorder(imagen, borde_size, borde_size, borde_size, borde_size, cv2.BORDER_CONSTANT, value=[0, 0, 0])

    imagen_tk = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)))
    panel.config(image=imagen_tk)
    panel.image = imagen_tk

def aplicar_ruido():
    if imagen is not None:
        cantidad_ruido = slider_ruido.get()
        rows, cols, channels = imagen.shape
        ruido = np.random.normal(0, cantidad_ruido, (rows, cols, channels))
        imagen_con_ruido = np.clip(imagen + ruido, 0, 255).astype(np.uint8)
        mostrar_imagen_cv(imagen_con_ruido, panel_ajustado, width=200, height=200)

def guardar_imagen():
    if imagen is not None:
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            cv2.imwrite(file_path, cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
            print(f"Imagen guardada en: {file_path}")


root = Tk()
root.title("Segmentador de Grietas")



panel_original = Label(root)
panel_original.grid(row=0, column=0, padx=10, pady=10)

panel_ajustado = Label(root)
panel_ajustado.grid(row=0, column=1, padx=10, pady=10)

btn_cargar = Button(root, text="Cargar Imagen", command=cargar_imagen)
btn_cargar.grid(row=1, column=0)


brillo_slider = Scale(root, from_=-100, to=100, orient=HORIZONTAL, command=actualizar_brillo_contraste, label="Brillo")
brillo_slider.grid(row=3, column=0, columnspan=2)
brillo_label = Label(root, text="Brillo: 0")
brillo_label.grid(row=4, column=0, columnspan=2)


contraste_slider = Scale(root, from_=-100, to=100, orient=HORIZONTAL, command=actualizar_brillo_contraste, label="Contraste")
contraste_slider.grid(row=3, column=1, columnspan=2)
contraste_label = Label(root, text="Contraste: 0")
contraste_label.grid(row=4, column=1, columnspan=2)



btn_ajuste = Button(root, text="Aplicar Ajuste", command=aplicar_ajuste, bg="blue", fg="white")
btn_ajuste.grid(row=3, column=2, rowspan=2)  

btn_grises = Button(root, text="Escala de Grises", command=aplicar_grises, bg="green", fg="white")
btn_grises.grid(row=0, column=2)

suavizar_slider = Scale(root, from_=1, to=10, orient=HORIZONTAL, label="Suavizar")
suavizar_slider.grid(row=2, column=1)

btn_suavizar = Button(root, text="Suavizar Imagen", command=aplicar_suavizado, bg="orange", fg="white")
btn_suavizar.grid(row=2, column=2)

apertura_slider = Scale(root, from_=1, to=10, orient=HORIZONTAL, label="Apertura")
apertura_slider.grid(row=5, column=1)

btn_apertura = Button(root, text="Aplicar Apertura", command=aplicar_apertura, bg="purple", fg="white")
btn_apertura.grid(row=5, column=2)

cierre_slider = Scale(root, from_=1, to=10, orient=HORIZONTAL, label="Cierre")
cierre_slider.grid(row=6, column=1)

btn_cierre = Button(root, text="Aplicar Cierre", command=aplicar_cierre, bg="red", fg="white")
btn_cierre.grid(row=6, column=2)

erosion_slider = Scale(root, from_=1, to=10, orient=HORIZONTAL, label="Erosión")
erosion_slider.grid(row=7, column=1)

btn_erosion = Button(root, text="Aplicar Erosión", command=aplicar_erosion, bg="yellow", fg="black")
btn_erosion.grid(row=7, column=2)

dilatacion_slider = Scale(root, from_=1, to=10, orient=HORIZONTAL, label="Dilatación")
dilatacion_slider.grid(row=8, column=1)

btn_dilatacion = Button(root, text="Aplicar Dilatación", command=aplicar_dilatacion, bg="cyan", fg="black")
btn_dilatacion.grid(row=8, column=2)


slider_ruido = Scale(root, from_=0, to=100, orient=HORIZONTAL, label="Cantidad de Ruido")
slider_ruido.grid(row=9, column=1)

btn_ruido = Button(root, text="Aplicar Ruido", command=aplicar_ruido, bg="purple", fg="white")
btn_ruido.grid(row=9, column=2)



btn_guardar = Button(root, text="Guardar Imagen", command=guardar_imagen, bg="purple", fg="white")
btn_guardar.grid(row=1, column=3)


root.mainloop()

