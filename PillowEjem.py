
from PIL import Image, ImageFilter

# Abrir la imagen original
image = Image.open("imagen.jpg")

# Mostrar la imagen original
image.show()

# 1. Redimensionar la imagen
image_resized = image.resize((800, 600))  # Nuevo tamaño de la imagen
image_resized.show()

# 2. Rotar la imagen 45 grados
image_rotated = image.rotate(45)  # Rotación en sentido horario
image_rotated.show()

# 3. Aplicar un filtro de desenfoque
image_blurred = image.filter(ImageFilter.BLUR)  # Filtro de desenfoque
image_blurred.show()

# 4. Recortar una sección de la imagen
left = 100
top = 100
right = 600
bottom = 500
image_cropped = image.crop((left, top, right, bottom))  # Coordenadas para el recorte
image_cropped.show()

# 5. Guardar las imágenes modificadas
image_resized.save("imagen_redimensionada.jpg")
image_rotated.save("imagen_rotada.jpg")
image_blurred.save("imagen_desenfocada.jpg")
image_cropped.save("imagen_recortada.jpg")
