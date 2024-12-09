from PIL import Image

# Cargar la imagen PNG
ruta_png = "calculadoradecosto.png"  # Cambia esto por la ruta de tu imagen
ruta_ico = "crk.ico"    # Cambia esto por el nombre de tu archivo .ico

# Convertir a ICO
imagen = Image.open(ruta_png)
imagen.save(ruta_ico, format="ICO", sizes=[(64, 64), (128, 128), (256, 256)])

print("El archivo se convirtió a .ico exitosamente.")
