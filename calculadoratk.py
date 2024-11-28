import tkinter as tk
from tkinter import simpledialog, messagebox

# Base de datos simulada de enlaces y precios
enlaces_y_precios = {
    "Teléfono": {"Pantalla": {"precio": 120, "enlace": "https://link-pantalla"},
                 "Batería": {"precio": 80, "enlace": "https://link-bateria"}},
    "Laptop": {"Pantalla": {"precio": 200, "enlace": "https://link-pantalla-laptop"},
               "Teclado": {"precio": 50, "enlace": "https://link-teclado"}},
    "Televisor": {"Pantalla": {"precio": 300, "enlace": "https://link-pantalla-tv"},
                  "Altavoces": {"precio": 100, "enlace": "https://link-altavoces"}}
}

# Función para abrir enlaces en el navegador
def abrir_enlace(url):
    import webbrowser
    webbrowser.open(url)

# Función para mostrar el desglose de costos y gestionar enlaces
def calcular_costos(dispositivo):
    def editar_enlace(componente):
        if componente in enlaces_y_precios[dispositivo]:
            nuevo_enlace = simpledialog.askstring("Editar Enlace", f"Introduce el nuevo enlace para {componente}:")
            if nuevo_enlace:
                enlaces_y_precios[dispositivo][componente]["enlace"] = nuevo_enlace
                messagebox.showinfo("Enlace Actualizado", f"El enlace para {componente} ha sido actualizado.")
                actualizar_componentes()

    def agregar_componente():
        nuevo_componente = simpledialog.askstring("Nuevo Componente", "Introduce el nombre del nuevo componente:")
        nuevo_precio = simpledialog.askfloat("Nuevo Precio", f"Introduce el precio para {nuevo_componente}:")
        nuevo_enlace = simpledialog.askstring("Nuevo Enlace", f"Introduce el enlace para {nuevo_componente}:")
        if nuevo_componente and nuevo_precio and nuevo_enlace:
            enlaces_y_precios[dispositivo][nuevo_componente] = {"precio": nuevo_precio, "enlace": nuevo_enlace}
            messagebox.showinfo("Componente Agregado", f"Se agregó {nuevo_componente} con su precio y enlace.")
            actualizar_componentes()

    def actualizar_componentes():
        for widget in frame_componentes.winfo_children():
            widget.destroy()
        
        total_costo = 0
        for componente, datos in enlaces_y_precios[dispositivo].items():
            total_costo += datos["precio"]
            
            componente_label = tk.Label(frame_componentes, text=f"• {componente}: ${datos['precio']}", 
                                         font=("Arial", 12), fg="blue", cursor="hand2", anchor="w")
            componente_label.pack(fill="x", padx=10, pady=5)
            componente_label.bind("<Button-1>", lambda e, url=datos["enlace"]: abrir_enlace(url))

            btn_editar = tk.Button(frame_componentes, text="Editar", font=("Arial", 10), bg="#FF9800", fg="white",
                                   command=lambda c=componente: editar_enlace(c))
            btn_editar.pack(pady=5, padx=20, anchor="e")
        
        label_total.config(text=f"Total Costo: ${total_costo:.2f}")
        btn_agregar.pack(pady=10)

    # Ventana de desglose de costos
    ventana_costos = tk.Toplevel()
    ventana_costos.title(f"Desglose de Costos - {dispositivo}")
    ventana_costos.geometry("400x600")
    ventana_costos.resizable(False, False)
    ventana_costos.config(bg="#ECEFF1")

    tk.Label(ventana_costos, text=f"Desglose de Costos para {dispositivo}", font=("Arial", 16, "bold"), 
             bg="#ECEFF1").pack(pady=10)
    
    # Frame con barra deslizadora
    frame_scroll = tk.Frame(ventana_costos)
    frame_scroll.pack(fill="both", expand=True, padx=10, pady=10)

    canvas = tk.Canvas(frame_scroll, bg="#ECEFF1")
    scrollbar = tk.Scrollbar(frame_scroll, orient="vertical", command=canvas.yview)
    frame_componentes = tk.Frame(canvas, bg="#ECEFF1")

    frame_componentes.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 0), window=frame_componentes, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    label_total = tk.Label(ventana_costos, text="", font=("Arial", 14), bg="#ECEFF1")
    label_total.pack(pady=10)

    btn_agregar = tk.Button(ventana_costos, text="Agregar Nuevo Componente", font=("Arial", 12), bg="#4CAF50", fg="white",
                            command=agregar_componente)
    
    actualizar_componentes()

# Ventana principal
def iniciar_calculadora():
    ventana = tk.Tk()
    ventana.title("CRK Calculadora de Costos")
    ventana.geometry("400x600")
    ventana.resizable(False, False)
    ventana.config(bg="#ECEFF1")

    dispositivos = ["Teléfono", "Laptop", "Televisor"]

    tk.Label(ventana, text="Selecciona un dispositivo:", font=("Arial", 14, "bold"), bg="#ECEFF1").pack(pady=20)
    dispositivo_var = tk.StringVar(value=dispositivos[0])
    tk.OptionMenu(ventana, dispositivo_var, *dispositivos).pack(pady=10)

    tk.Button(ventana, text="Calcular Costos", font=("Arial", 12), bg="#4CAF50", fg="white",
              command=lambda: calcular_costos(dispositivo_var.get())).pack(pady=20)

    # Etiqueta de créditos en la parte inferior
    tk.Label(ventana, text="Hecho por: Rohelys Armas, Carlos Goitia y Kevin Sifontes", 
             font=("Arial", 10, "italic"), bg="#ECEFF1").pack(side="bottom", pady=10)

    ventana.mainloop()

# Iniciar la calculadora
iniciar_calculadora()
