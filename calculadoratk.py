import tkinter as tk
from tkinter import messagebox

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

# Función para calcular costo
def calcular_costo():
    dispositivo = dispositivo_var.get().lower()
    if dispositivo in components_database:
        total = 0
        componentes = components_database[dispositivo]
        resultado = f"Componentes de {dispositivo.capitalize()}:\n"
        for componente, (precio, _) in componentes.items():
            resultado += f"{componente}: ${precio}\n"
            total += precio
        resultado += f"\nCosto total: ${total}"
        messagebox.showinfo("Costo Total", resultado)
    else:
        messagebox.showerror("Error", "Dispositivo no encontrado")

# Crear ventana principal
root = tk.Tk()
root.title("Calculadora de Costos Electrónicos")

# Elementos de la ventana
dispositivo_var = tk.StringVar()
label = tk.Label(root, text="Selecciona el dispositivo")
label.pack(pady=10)

dispositivo_entry = tk.Entry(root, textvariable=dispositivo_var)
dispositivo_entry.pack(pady=10)

calcular_button = tk.Button(root, text="Calcular Costo", command=calcular_costo)
calcular_button.pack(pady=10)

# Ejecutar la ventana
root.mainloop()


