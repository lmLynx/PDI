import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk, ImageOps
import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os

# Importar las clases de los algoritmos
from Filtro_de_Robinson2 import FiltroRobinson
from Filtro_Umbralado2 import FiltroUmbralado
from filtromin2 import FiltroMin
from Gamma2 import Gama

# Función para cargar una imagen
def load_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.bmp")])
    if file_path:
        img = cv2.imread(file_path)
        return img, file_path
    return None, None

# Función para mostrar la imagen en la interfaz
def display_image(img, label, max_size=(400, 400)):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    img_pil.thumbnail(max_size, Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img_pil)
    label.config(image=img_tk)
    label.image = img_tk

# Función para mostrar el histograma de una imagen en la interfaz
def display_histogram(img, label):
    fig, ax = plt.subplots()
    if len(img.shape) == 2:  # Grayscale image
        ax.hist(img.ravel(), bins=256, color='black', alpha=0.7)
    else:  # Color image
        colors = ('r', 'g', 'b')
        for i, color in enumerate(colors):
            ax.hist(img[:, :, i].ravel(), bins=256, color=color, alpha=0.7)
    ax.set_xlim([0, 256])
    ax.set_ylim([0, None])
    fig.tight_layout()
    
    canvas = FigureCanvasTkAgg(fig, master=label)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Crear la ventana principal
root = tk.Tk()
root.title("Procesamiento Digital de Imágenes")

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

# Añadir el control de pestañas a la ventana principal
tab_control.pack(expand=1, fill="both")

# Añadir la imagen de fondo a la portada
background_image = Image.open("fondo.jpg")
background_image = ImageOps.fit(background_image, (800, 600), Image.LANCZOS)
background_image = ImageTk.PhotoImage(background_image)
background_label = tk.Label(tab_portada, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Añadir el título y cambiar la fuente
title = tk.Label(tab_portada, text="Segmentación de Zonas con presencia\nde incendios forestales en tomas satelitales",
                 font=("Helvetica", 18, "bold"))
title.pack(pady=20)

# Añadir la información de la comunidad
info = tk.Label(tab_portada, text="Comunidad 7:\n• Díaz Martínez Aldo\n• Lagunes Vázquez Mildred Valeria\n• Lezama Tapia Brisa María.\n• Meléndez Medina Jimena\n• Pérez Aguirre Ian Miztli.", 
                justify="left", font=("Helvetica", 14), bg="white")
info.pack(pady=10)

# Añadir el texto "Seleccione una imagen para modificar"
select_text = tk.Label(tab_portada, text="Seleccione una imagen para modificar", font=("Helvetica", 12), bg="white")
select_text.pack(pady=10)

# Selector de archivos
file_path = None
selected_img = None

def select_file():
    global file_path, selected_img
    selected_img, file_path = load_image()
    if selected_img is not None:
        legend_text.set(f"Imagen ({os.path.basename(file_path)}) cargada correctamente")
        apply_algorithms()

file_selector = tk.Button(tab_portada, text="Seleccionar Imagen", command=select_file)
file_selector.pack(pady=10)

# Leyenda para mostrar el nombre del archivo cargado
legend_text = tk.StringVar()
legend_label = tk.Label(tab_portada, textvariable=legend_text, font=("Helvetica", 12), bg="white")
legend_label.pack(pady=10)

# Instanciar las clases de los algoritmos
filtro_robinson = FiltroRobinson()
filtro_umbralado = FiltroUmbralado()
filtro_min = FiltroMin()
gama = Gama()

# Función para aplicar los algoritmos y mostrar los resultados
def apply_algorithms():
    if selected_img is not None:
        # Aplicar y mostrar resultados para cada algoritmo
        display_algorithm_results(filtro_robinson, img_label_robinson_original, hist_label_robinson_original, img_label_robinson_processed, hist_label_robinson_processed)
        display_algorithm_results(filtro_umbralado, img_label_umbralado_original, hist_label_umbralado_original, img_label_umbralado_processed, hist_label_umbralado_processed)
        display_algorithm_results(filtro_min, img_label_min_original, hist_label_min_original, img_label_min_processed, hist_label_min_processed)
        display_algorithm_results(gama, img_label_gama_original, hist_label_gama_original, img_label_gama_processed, hist_label_gama_processed)

def display_algorithm_results(algorithm, original_img_label, original_hist_label, processed_img_label, processed_hist_label):
    # Mostrar imagen original y su histograma
    display_image(selected_img, original_img_label)
    display_histogram(selected_img, original_hist_label)

    # Aplicar algoritmo y mostrar imagen procesada y su histograma
    processed_img = algorithm.aplicar(selected_img)
    display_image(processed_img, processed_img_label)
    display_histogram(processed_img, processed_hist_label)

# Crear una cuadrícula para cada pestaña
def create_grid(tab):
    original_img_label = tk.Label(tab)
    original_img_label.grid(row=0, column=0, padx=10, pady=10)

    original_hist_label = tk.Label(tab)
    original_hist_label.grid(row=1, column=0, padx=10, pady=10)

    processed_img_label = tk.Label(tab)
    processed_img_label.grid(row=0, column=1, padx=10, pady=10)

    processed_hist_label = tk.Label(tab)
    processed_hist_label.grid(row=1, column=1, padx=10, pady=10)

    return original_img_label, original_hist_label, processed_img_label, processed_hist_label

# Crear cuadrículas para cada pestaña
img_label_robinson_original, hist_label_robinson_original, img_label_robinson_processed, hist_label_robinson_processed = create_grid(tab_robinson)
img_label_umbralado_original, hist_label_umbralado_original, img_label_umbralado_processed, hist_label_umbralado_processed = create_grid(tab_umbralado)
img_label_min_original, hist_label_min_original, img_label_min_processed, hist_label_min_processed = create_grid(tab_min)
img_label_gama_original, hist_label_gama_original, img_label_gama_processed, hist_label_gama_processed = create_grid(tab_gama)

# Ajustar el tamaño de la ventana al contenido
root.update_idletasks()
root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")

# Ejecutar la ventana principal
root.mainloop()
