import tkinter as tk
from tkinter import ttk, messagebox

# Base de datos simulada (componentes y enlaces)
components_database = {
    'telefono': {
        'Pantalla': (50.0, 'https://www.mercadolibre.com.ve/pantalla-telefono'),
        'Batería': (20.0, 'https://www.mercadolibre.com.ve/bateria-telefono'),
        'Cámara': (35.0, 'https://www.mercadolibre.com.ve/camara-telefono'),
        'Procesador': (100.0, 'https://www.mercadolibre.com.ve/procesador-telefono'),
        'Memoria RAM': (30.0, 'https://www.mercadolibre.com.ve/ram-telefono'),
        'Almacenamiento': (40.0, 'https://www.mercadolibre.com.ve/almacenamiento-telefono')
    },
    'laptop': {
        'Pantalla': (150.0, 'https://www.mercadolibre.com.ve/pantalla-laptop'),
        'Teclado': (25.0, 'https://www.mercadolibre.com.ve/teclado-laptop'),
        'Batería': (60.0, 'https://www.mercadolibre.com.ve/bateria-laptop'),
        'Procesador': (200.0, 'https://www.mercadolibre.com.ve/procesador-laptop'),
        'Memoria RAM': (80.0, 'https://www.mercadolibre.com.ve/ram-laptop'),
        'Almacenamiento SSD': (120.0, 'https://www.mercadolibre.com.ve/almacenamiento-laptop'),
        'Tarjeta Gráfica': (300.0, 'https://www.mercadolibre.com.ve/tarjeta-grafica-laptop')
    },
    'televisor': {
        'Pantalla': (200.0, 'https://www.mercadolibre.com.ve/pantalla-televisor'),
        'Placa Base': (80.0, 'https://www.mercadolibre.com.ve/placa-base-televisor'),
        'Fuente de Alimentación': (50.0, 'https://www.mercadolibre.com.ve/fuente-televisor'),
        'Altavoces': (30.0, 'https://www.mercadolibre.com.ve/altavoces-televisor'),
        'Sintonizador': (40.0, 'https://www.mercadolibre.com.ve/sintonizador-televisor'),
        'Carcasa': (60.0, 'https://www.mercadolibre.com.ve/carcasa-televisor')
    }
}

# Función para calcular el costo del dispositivo seleccionado
def calcular_costo():
    dispositivo = dispositivo_var.get().lower()
    
    if dispositivo in components_database:
        total = 0
        componentes = components_database[dispositivo]
        componentes_text = ""
        
        for componente, (precio, _) in componentes.items():
            componentes_text += f"{componente}: ${precio}\n"
            total += precio
        
        resultado_label.config(text=f"Componentes de {dispositivo.capitalize()}:\n{componentes_text}\nCosto total: ${total}")
        
        comprar_button.config(state=tk.NORMAL)  # Habilitar botón de compra
    else:
        messagebox.showerror("Error", "El dispositivo no está en la base de datos")

# Función para mostrar los enlaces de compra
def mostrar_enlaces():
    dispositivo = dispositivo_var.get().lower()
    
    if dispositivo in components_database:
        enlaces_text = ""
        for componente, (_, link) in components_database[dispositivo].items():
            enlaces_text += f"{componente}: {link}\n"
        
        messagebox.showinfo("Enlaces de Compra", enlaces_text)

# Crear ventana principal
root = tk.Tk()
root.title("Calculadora de Costos Electrónicos")

# Etiqueta de título
titulo_label = tk.Label(root, text="Calculadora de Costos Electrónicos", font=("Helvetica", 16))
titulo_label.pack(pady=10)

# Menú desplegable para seleccionar dispositivo
dispositivo_var = tk.StringVar()
dispositivo_var.set("Selecciona un dispositivo")  # Valor por defecto

dispositivo_label = tk.Label(root, text="Selecciona un dispositivo:")
dispositivo_label.pack()

dispositivo_menu = ttk.Combobox(root, textvariable=dispositivo_var)
dispositivo_menu['values'] = ['Telefono', 'Laptop', 'Televisor']  # Opciones
dispositivo_menu.pack(pady=5)

# Botón para calcular el costo
calcular_button = tk.Button(root, text="Calcular Costo", command=calcular_costo)
calcular_button.pack(pady=10)

# Label para mostrar los componentes y el costo total
resultado_label = tk.Label(root, text="", justify="left")
resultado_label.pack(pady=10)

# Botón para mostrar enlaces de compra (deshabilitado hasta que se calcule)
comprar_button = tk.Button(root, text="Mostrar Enlaces de Compra", state=tk.DISABLED, command=mostrar_enlaces)
comprar_button.pack(pady=10)

# Ejecutar la ventana
root.mainloop()


