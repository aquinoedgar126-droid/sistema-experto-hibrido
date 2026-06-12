import tkinter as tk
from tkinter import messagebox
from estilos import *

def diagnosticar():
    sintomas_seleccionados = []

    for sintoma, variable in sintomas.items():
        if variable.get() == 1:
            sintomas_seleccionados.append(sintoma)

    if not sintomas_seleccionados:
        messagebox.showwarning("Aviso", "Selecciona al menos un síntoma.")
        return

    categoria = "Desconocido"
    causa = "No se pudo identificar una causa específica."
    recomendacion = "Revisar físicamente el equipo o agregar más síntomas."

    if "No enciende" in sintomas_seleccionados or "No hay luces" in sintomas_seleccionados:
        categoria = "Sin energía"
        causa = "Fuente de poder, cable de corriente, regulador o tarjeta madre."
        recomendacion = "Verificar cable, contacto eléctrico, regulador y fuente ATX."

    elif "Pantalla negra" in sintomas_seleccionados or "No da video" in sintomas_seleccionados:
        categoria = "Falla de video"
        causa = "Memoria RAM, monitor, cable HDMI/VGA o tarjeta gráfica."
        recomendacion = "Limpiar RAM, revisar cable de video y probar otro monitor."

    elif "Pitidos al encender" in sintomas_seleccionados:
        categoria = "Problema de RAM"
        causa = "Memoria RAM mal colocada, dañada o incompatible."
        recomendacion = "Retirar la RAM, limpiar contactos y volver a instalarla."

    elif "No detecta disco" in sintomas_seleccionados:
        categoria = "Problema de disco"
        causa = "Disco duro/SSD, cable SATA, alimentación o configuración BIOS."
        recomendacion = "Revisar cables, entrar al BIOS y probar el disco en otro equipo."

    elif "Se reinicia constantemente" in sintomas_seleccionados:
        categoria = "Reinicio constante"
        causa = "Fuente inestable, sobrecalentamiento o falla en procesador."
        recomendacion = "Revisar ventiladores, temperatura y fuente de alimentación."

    elif "Se calienta demasiado" in sintomas_seleccionados:
        categoria = "Sobrecalentamiento"
        causa = "Ventilador sucio, pasta térmica seca o acumulación de polvo."
        recomendacion = "Limpiar ventiladores, cambiar pasta térmica y revisar flujo de aire."

    texto_resultado.config(
        text=f"Síntomas seleccionados:\n- " + "\n- ".join(sintomas_seleccionados) +
             f"\n\nCategoría detectada:\n{categoria}" +
             f"\n\nPosible causa:\n{causa}" +
             f"\n\nRecomendación:\n{recomendacion}"
    )

def limpiar():
    for variable in sintomas.values():
        variable.set(0)

    texto_resultado.config(
        text="Selecciona los síntomas observados y presiona Diagnosticar."
    )

ventana = tk.Tk()
ventana.title("Sistema Experto Híbrido")
ventana.geometry("800x600")
ventana.resizable(False, False)
ventana.configure(bg=COLOR_FONDO)

titulo = tk.Label(
    ventana,
    text="Sistema Experto Híbrido",
    font=FUENTE_TITULO,
    bg=COLOR_FONDO,
    fg=COLOR_TEXTO_CLARO
)
titulo.pack(pady=(25, 5))

subtitulo = tk.Label(
    ventana,
    text="Diagnóstico de fallas de encendido en computadoras",
    font=FUENTE_SUBTITULO,
    bg=COLOR_FONDO,
    fg=COLOR_TEXTO_GRIS
)
subtitulo.pack(pady=(0, 20))

contenedor = tk.Frame(
    ventana,
    bg=COLOR_PANEL,
    padx=25,
    pady=20
)
contenedor.pack(padx=40, pady=10, fill="x")

label_sintomas = tk.Label(
    contenedor,
    text="Selecciona los síntomas observados:",
    font=("Arial", 13, "bold"),
    bg=COLOR_PANEL,
    fg=COLOR_TEXTO_CLARO
)
label_sintomas.pack(anchor="w", pady=(0, 10))

tabla = tk.Frame(contenedor, bg=COLOR_PANEL)
tabla.pack(fill="x")

lista_sintomas = [
    "No enciende",
    "No hay luces",
    "Pantalla negra",
    "No da video",
    "Pitidos al encender",
    "No detecta disco",
    "Se reinicia constantemente",
    "Se calienta demasiado"
]

sintomas = {}

for i, sintoma in enumerate(lista_sintomas):
    variable = tk.IntVar()
    sintomas[sintoma] = variable

    fila = i // 2
    columna = i % 2

    check = tk.Checkbutton(
        tabla,
        text=sintoma,
        variable=variable,
        font=FUENTE_NORMAL,
        bg=COLOR_PANEL,
        fg=COLOR_TEXTO_CLARO,
        selectcolor=COLOR_FONDO,
        activebackground=COLOR_PANEL,
        activeforeground=COLOR_TEXTO_CLARO
    )
    check.grid(row=fila, column=columna, sticky="w", padx=20, pady=6)

frame_botones = tk.Frame(contenedor, bg=COLOR_PANEL)
frame_botones.pack(pady=15)

boton_diagnosticar = tk.Button(
    frame_botones,
    text="Diagnosticar",
    font=FUENTE_BOTON,
    bg=COLOR_BOTON,
    fg=COLOR_TEXTO_CLARO,
    activebackground=COLOR_BOTON_HOVER,
    activeforeground=COLOR_TEXTO_CLARO,
    relief="flat",
    width=18,
    command=diagnosticar
)
boton_diagnosticar.grid(row=0, column=0, padx=10, ipady=6)

boton_limpiar = tk.Button(
    frame_botones,
    text="Limpiar",
    font=FUENTE_BOTON,
    bg="#475569",
    fg=COLOR_TEXTO_CLARO,
    activebackground="#334155",
    activeforeground=COLOR_TEXTO_CLARO,
    relief="flat",
    width=18,
    command=limpiar
)
boton_limpiar.grid(row=0, column=1, padx=10, ipady=6)

resultado_frame = tk.Frame(
    ventana,
    bg=COLOR_TARJETA,
    padx=25,
    pady=20
)
resultado_frame.pack(padx=40, pady=20, fill="both")

texto_resultado = tk.Label(
    resultado_frame,
    text="Selecciona los síntomas observados y presiona Diagnosticar.",
    font=FUENTE_RESULTADO,
    bg=COLOR_TARJETA,
    fg=COLOR_TEXTO_OSCURO,
    justify="left",
    wraplength=700
)
texto_resultado.pack(anchor="w")

footer = tk.Label(
    ventana,
    text="SWI-Prolog + CLIPS + Python Tkinter",
    font=("Arial", 10),
    bg=COLOR_FONDO,
    fg="#94a3b8"
)
footer.pack(side="bottom", pady=10)

ventana.mainloop()