import tkinter as tk
from tkinter import ttk, messagebox
import ttkbootstrap as tb  # Librería para mejorar la interfaz gráfica
from pint import UnitRegistry  # Librería para conversión de unidades

# Configuración de Pint
ureg = UnitRegistry()

# Función para realizar la conversión
def convert():
    try:
        value = float(entry_value.get())  # Obtener el valor ingresado
        from_unit = from_unit_combobox.get().lower()  # Convertir a minúsculas
        to_unit = to_unit_combobox.get().lower()

        # Manejo especial para temperaturas
        if from_unit == "celsius" and to_unit == "fahrenheit":
            result = (value * 9/5) + 32  # Fórmula de Celsius a Fahrenheit
        elif from_unit == "fahrenheit" and to_unit == "celsius":
            result = (value - 32) * 5/9  # Fórmula de Fahrenheit a Celsius
        else:
            # Para otras conversiones usando Pint
            result = (value * ureg(from_unit)).to(to_unit).magnitude

        # Mostrar el resultado con 4 decimales
        result_label.config(text=f"Resultado: {result:.4f} {to_unit}")

    except ValueError:
        messagebox.showwarning("Advertencia", "Por favor ingresa un valor numérico válido.")
    except:
        messagebox.showerror("Error", "Conversión no soportada.")

# Crear la interfaz gráfica con ttkbootstrap
root = tb.Window(themename="cyborg")  # Tema moderno
root.title("Conversor de Unidades")
root.geometry("450x400")

# Contenedor principal
frame = ttk.Frame(root, padding=20)
frame.pack(pady=20)

# Título
title_label = ttk.Label(frame, text="Conversor de Unidades", font=("Arial", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Campo para ingresar el valor a convertir
entry_label = ttk.Label(frame, text="Valor a Convertir:", font=("Arial", 12))
entry_label.grid(row=1, column=0, pady=5, sticky="w")
entry_value = ttk.Entry(frame, width=20, font=("Arial", 12))
entry_value.grid(row=1, column=1, pady=5)

# Selección de unidades de origen
from_unit_label = ttk.Label(frame, text="Unidad de origen:", font=("Arial", 12))
from_unit_label.grid(row=2, column=0, pady=5, sticky="w")
from_unit_combobox = ttk.Combobox(
    frame, values=["Celsius", "Fahrenheit", "meters", "kilometers", "grams", "kilograms"],
    state="readonly", font=("Arial", 12)
)
from_unit_combobox.grid(row=2, column=1, pady=5)
from_unit_combobox.set("Celsius")  # Valor predeterminado

# Selección de unidades de destino
to_unit_label = ttk.Label(frame, text="Unidad de destino:", font=("Arial", 12))
to_unit_label.grid(row=3, column=0, pady=5, sticky="w")
to_unit_combobox = ttk.Combobox(
    frame, values=["Celsius", "Fahrenheit", "meters", "kilometers", "grams", "kilograms"],
    state="readonly", font=("Arial", 12)
)
to_unit_combobox.grid(row=3, column=1, pady=5)
to_unit_combobox.set("Fahrenheit")  # Valor predeterminado

# Botón para realizar la conversión
convert_button = tb.Button(
    frame, text="Calcular", command=convert, bootstyle="primary", width=18
)
convert_button.grid(row=4, column=0, columnspan=2, pady=15)

# Etiqueta para mostrar el resultado
result_label = ttk.Label(frame, text="Resultado: ", font=("Arial", 12, "bold"), foreground="#FFD700")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Iniciar la interfaz gráfica
root.mainloop()
