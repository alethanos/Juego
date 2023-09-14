import random
import tkinter as tk
from tkinter import ttk

# Lista de animales para adivinar
animales = [
    "titi",
    "vicuña",
    "condor",
    "bufeo",
    "taruca",
    "jaguar",
    "puma",
    "tapir",
    "chinchilla",
    "tinamou",
    "monito",
    "tapacari",
    "campanero",
    "matraca"
]

# Función para seleccionar un animal al azar
def seleccionar_animal():
    return random.choice(animales)

# Función para ocultar el nombre del animal con guiones bajos
def ocultar_nombre(animal):
    return "_" * len(animal)

# Función para mostrar el estado actual del juego
def mostrar_juego():
    lbl_palabra.config(text=f"Palabra: {nombre_oculto}")
    lbl_intentos.config(text=f"Intentos restantes: {intentos_restantes}")

# Función para comenzar un nuevo juego
def nuevo_juego():
    global animal_seleccionado, nombre_oculto, intentos_restantes
    animal_seleccionado = seleccionar_animal()
    nombre_oculto = ocultar_nombre(animal_seleccionado)
    intentos_restantes = 6  # Puedes ajustar el número de intentos permitidos
    mostrar_juego()
    btn_adivinar.config(state=tk.NORMAL)
    btn_nuevo_juego.config(state=tk.DISABLED)

# Función para manejar la adivinanza de letras
def adivinar_letra():
    global intentos_restantes, nombre_oculto

    letra = entry_letra.get().lower()
    entry_letra.delete(0, tk.END)

    if letra.isalpha() and len(letra) == 1:
        if letra in animal_seleccionado:
            for i in range(len(animal_seleccionado)):
                if animal_seleccionado[i] == letra:
                    nombre_oculto = nombre_oculto[:i] + letra + nombre_oculto[i + 1:]
            lbl_palabra.config(text=f"Palabra: {nombre_oculto}")
            if nombre_oculto == animal_seleccionado:
                lbl_mensaje.config(text=f"¡Ganaste! El animal es {animal_seleccionado}.")
                btn_adivinar.config(state=tk.DISABLED)
                btn_nuevo_juego.config(state=tk.NORMAL)
        else:
            intentos_restantes -= 1
            lbl_intentos.config(text=f"Intentos restantes: {intentos_restantes}")
            if intentos_restantes == 0:
                lbl_mensaje.config(text=f"¡Perdiste! El animal era {animal_seleccionado}.")
                btn_adivinar.config(state=tk.DISABLED)
                btn_nuevo_juego.config(state=tk.NORMAL)
    else:
        lbl_mensaje.config(text="Ingresa una letra válida.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Adivina el Animal")

# Variables globales
animal_seleccionado = ""
nombre_oculto = ""
intentos_restantes = 0

# Crear un frame para agrupar los elementos
frame = tk.Frame(ventana)
frame.pack(padx=20, pady=20)

# Crear un frame interno para los demás elementos
frame_interno = tk.Frame(frame)
frame_interno.grid(row=0, column=0, padx=10, pady=10)

# Crear una etiqueta para mostrar la palabra oculta
lbl_palabra = tk.Label(frame_interno, text="", font=("Arial", 16))
lbl_palabra.grid(row=0, column=0, pady=5)

# Crear una etiqueta para mostrar los intentos restantes
lbl_intentos = tk.Label(frame_interno, text="", font=("Arial", 16))
lbl_intentos.grid(row=1, column=0, pady=5)

# Crear una etiqueta para mostrar mensajes del juego
lbl_mensaje = tk.Label(frame_interno, text="", font=("Arial", 16))
lbl_mensaje.grid(row=2, column=0, pady=5)

# Crear una entrada de texto para ingresar letras
entry_letra = tk.Entry(frame_interno, font=("Arial", 16))
entry_letra.grid(row=3, column=0, pady=5)

# Crear un botón para adivinar una letra
btn_adivinar = tk.Button(frame_interno, text="Probar", command=adivinar_letra, font=("Arial", 16))
btn_adivinar.grid(row=4, column=0, pady=5)

# Crear un botón para comenzar un nuevo juego
btn_nuevo_juego = tk.Button(frame_interno, text="Jugar de nuevo", command=nuevo_juego, state=tk.DISABLED, font=("Arial", 16))
btn_nuevo_juego.grid(row=5, column=0, pady=5)

# Crear una lista de opciones como ayuda o referencia a la derecha
lista_opciones = tk.Listbox(frame, selectbackground="blue")  # Color de fondo de selección azul
for animal in animales:
    lista_opciones.insert(tk.END, animal)
lista_opciones.grid(row=0, column=1, rowspan=6, padx=10)

# Iniciar el primer juego
nuevo_juego()

# Ejecutar la ventana principal
ventana.mainloop()
