from PIL import Image, ImageFilter

# Cargar la imagen
image_path = './incendio4.jpg'
image = Image.open(image_path)

# Aplicar el filtro mínimo
min_filter_image = image.filter(ImageFilter.MinFilter)

# Guardar la imagen procesada
min_filter_image_path = './incendio4_con_filtro.jpg'
min_filter_image.show(min_filter_image_path)
min_filter_image.save(min_filter_image_path)

min_filter_image_path
