# Base de datos simulada (ejemplo con algunos componentes)
components_database = {
    'telefono': {
        'Pantalla': 50.0,  # precio en USD
        'Batería': 20.0,
        'Cámara': 35.0,
        'Procesador': 100.0,
        'Memoria RAM': 30.0,
        'Almacenamiento': 40.0
    },
    'laptop': {
        'Pantalla': 150.0,
        'Teclado': 25.0,
        'Batería': 60.0,
        'Procesador': 200.0,
        'Memoria RAM': 80.0,
        'Almacenamiento SSD': 120.0,
        'Tarjeta Gráfica': 300.0
    },
    'televisor': {
        'Pantalla': 200.0,
        'Placa Base': 80.0,
        'Fuente de Alimentación': 50.0,
        'Altavoces': 30.0,
        'Sintonizador': 40.0,
        'Carcasa': 60.0
    }
}

# Función para calcular el costo total de un dispositivo
def calcular_costo_dispositivo(dispositivo):
    if dispositivo in components_database:
        print(f"Componentes de {dispositivo.capitalize()}:")
        total = 0
        for componente, precio in components_database[dispositivo].items():
            print(f"{componente}: ${precio}")
            total += precio
        print(f"\nCosto total de {dispositivo.capitalize()}: ${total}\n")
    else:
        print(f"El dispositivo '{dispositivo}' no está en la base de datos.\n")

# Función para buscar un componente específico
def buscar_componente(componente):
    encontrado = False
    for dispositivo, componentes in components_database.items():
        if componente in componentes:
            print(f"El componente '{componente}' está en '{dispositivo.capitalize()}' y cuesta ${componentes[componente]}")
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
main()
