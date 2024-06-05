import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np
import os

# Función para cargar una imagen
def load_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.bmp")])
    if file_path:
        img = cv2.imread(file_path)
        return img, file_path
    return None, None

# Función para mostrar la imagen en la interfaz
def display_image(img, label):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    img_tk = ImageTk.PhotoImage(img_pil)
    label.config(image=img_tk)
    label.image = img_tk

# Funciones de los algoritmos (simplificadas para el ejemplo)
def filtro_robinson(img):
    # Procesamiento de la imagen
    return img

def filtro_umbralado(img):
    # Procesamiento de la imagen
    return img

def filtro_min(img):
    # Procesamiento de la imagen
    return img

def gama(img):
    # Procesamiento de la imagen
    return img

def grietas_pdi(img):
    # Procesamiento de la imagen
    return img

# Crear la ventana principal
root = tk.Tk()
root.title("Procesamiento Digital de Imágenes")
root.geometry("800x600")

# Crear el widget de pestañas
tab_control = ttk.Notebook(root)

# Pestaña de portada
tab_portada = ttk.Frame(tab_control)
tab_control.add(tab_portada, text="Portada")

# Pestaña de Filtro Robinson
tab_robinson = ttk.Frame(tab_control)
tab_control.add(tab_robinson, text="Filtro de Robinson")

# Pestaña de Filtro Umbralado
tab_umbralado = ttk.Frame(tab_control)
tab_control.add(tab_umbralado, text="Filtro Umbralado")

# Pestaña de Filtro Mínimo
tab_min = ttk.Frame(tab_control)
tab_control.add(tab_min, text="Filtro Mínimo")

# Pestaña de Gama
tab_gama = ttk.Frame(tab_control)
tab_control.add(tab_gama, text="Gama")

# Pestaña de Grietas PDI
tab_grietas = ttk.Frame(tab_control)
tab_control.add(tab_grietas, text="Grietas PDI")

# Añadir el control de pestañas a la ventana principal
tab_control.pack(expand=1, fill="both")

# Añadir la información de la portada
info = tk.Label(tab_portada, text="Comunidad 7:\n• Díaz Martínez Aldo\n• Lagunes Vázquez Mildred Valeria\n• Lezama Tapia Brisa María.\n• Meléndez Medina Jimena\n• Pérez Aguirre Ian Miztli.", justify="left", font=("Helvetica", 14))
info.pack(pady=20)

# Selector de archivos
file_path = None
selected_img = None

def select_file():
    global file_path, selected_img
    selected_img, file_path = load_image()
    if selected_img is not None:
        display_image(selected_img, img_label_portada)
        apply_algorithms()

file_selector = tk.Button(tab_portada, text="Seleccionar Imagen", command=select_file)
file_selector.pack(pady=20)

# Etiqueta para mostrar la imagen en la portada
img_label_portada = tk.Label(tab_portada)
img_label_portada.pack()

# Función para aplicar los algoritmos y mostrar los resultados
def apply_algorithms():
    if selected_img is not None:
        # Aplicar y mostrar Filtro Robinson
        img_robinson = filtro_robinson(selected_img)
        display_image(img_robinson, img_label_robinson)

        # Aplicar y mostrar Filtro Umbralado
        img_umbralado = filtro_umbralado(selected_img)
        display_image(img_umbralado, img_label_umbralado)

        # Aplicar y mostrar Filtro Mínimo
        img_min = filtro_min(selected_img)
        display_image(img_min, img_label_min)

        # Aplicar y mostrar Gama
        img_gama = gama(selected_img)
        display_image(img_gama, img_label_gama)

        # Aplicar y mostrar Grietas PDI
        img_grietas = grietas_pdi(selected_img)
        display_image(img_grietas, img_label_grietas)

# Etiquetas para mostrar los resultados en cada pestaña
img_label_robinson = tk.Label(tab_robinson)
img_label_robinson.pack()

img_label_umbralado = tk.Label(tab_umbralado)
img_label_umbralado.pack()

img_label_min = tk.Label(tab_min)
img_label_min.pack()

img_label_gama = tk.Label(tab_gama)
img_label_gama.pack()

img_label_grietas = tk.Label(tab_grietas)
img_label_grietas.pack()

# Ejecutar la ventana principal
root.mainloop()
