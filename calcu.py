# Base de datos simulada (ejemplo con algunos componentes y enlaces de compra)
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

# Función para calcular el costo total de un dispositivo
def calcular_costo_dispositivo(dispositivo):
    if dispositivo in components_database:
        print(f"Componentes de {dispositivo.capitalize()}:")
        total = 0
        for componente, (precio, link) in components_database[dispositivo].items():
            print(f"{componente}: ${precio}")
            total += precio
        print(f"\nCosto total de {dispositivo.capitalize()}: ${total}\n")

        # Pregunta si desea comprar alguno de los componentes
        desea_comprar = input("¿Desea comprar alguno de estos componentes? (1. Sí / 2. No): ")

        if desea_comprar == '1':
            print("\nEnlaces para comprar los componentes:")
            for componente, (_, link) in components_database[dispositivo].items():
                print(f"{componente}: {link}")
            print("\nVolviendo al menú principal...\n")

        elif desea_comprar == '2':
            print("\nVolviendo al menú principal...\n")

        else:
            print("\nOpción no válida. Volviendo al menú principal...\n")
    else:
        print(f"El dispositivo '{dispositivo}' no está en la base de datos.\n")

# Función para buscar un componente específico
def buscar_componente(componente):
    encontrado = False
    for dispositivo, componentes in components_database.items():
        if componente in componentes:
            precio, link = componentes[componente]
            print(f"El componente '{componente}' está en '{dispositivo.capitalize()}' y cuesta ${precio} (Compra aquí: {link})")
            encontrado = True
    if not encontrado:
        print(f"El componente '{componente}' no se encuentra en la base de datos.\n")

# Interfaz principal
def main():
    print("Bienvenido a la Calculadora de Costos Electrónicos")
    
    while True:
        print("\n¿Qué te gustaría hacer?")
        print("1. Calcular el costo total de un dispositivo")
        print("2. Buscar el costo de un componente específico")
        print("3. Salir")
        opcion = input("Elige una opción (1/2/3): ")
        
        if opcion == '1':
            dispositivo = input("Ingresa el nombre del dispositivo (telefono/laptop/televisor): ").lower()
            calcular_costo_dispositivo(dispositivo)
        
        elif opcion == '2':
            componente = input("Ingresa el nombre del componente que deseas buscar: ").capitalize()
            buscar_componente(componente)
        
        elif opcion == '3':
            print("Gracias por usar la Calculadora de Costos Electrónicos. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Inténtalo de nuevo.\n")

# Ejecutar el programa

