from tkinter import Tk, Button, Entry

# Función para evaluar y mostrar el resultado en la pantalla
def calcular():
    expresion = pantalla.get()
    try:
        resultado = eval(expresion)
        pantalla.delete(0, "end")
        pantalla.insert("end", str(resultado))
    except:
        pantalla.delete(0, "end")
        pantalla.insert("end", "Error")

# Función para agregar un dígito a la pantalla
def agregar_digito(digito):
    pantalla.insert("end", digito)

# Función para agregar un operador a la pantalla
def agregar_operador(operador):
    expresion = pantalla.get()
    if expresion and expresion[-1] not in ["+", "-", "*", "/"]:
        pantalla.insert("end", operador)

# Configuración de la ventana principal
root = Tk()
root.title("Calculadora")
root.resizable(0, 0)
root.geometry("315x280")

# Configuración de la pantalla de salida
pantalla = Entry(root, width=22, bg="black", fg="white", borderwidth=0, font=("Arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=0)

# Configuración de los botones numéricos
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_digito("1"))
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_digito("2"))
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_digito("3"))
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_digito("4"))
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_digito("5"))
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_digito("6"))
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_digito("7"))
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_digito("8"))
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_digito("9"))

# Configuración de los botones de operaciones
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor="hand2", command=calcular)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0, command=lambda: agregar_digito("."))
boton_suma = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: agregar_operador("+"))
boton_resta = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: agregar_operador("-"))
boton_multiplicacion = Button(root, text="*", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: agregar_operador("*"))
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: agregar_operador("/"))

# Ubicación de los botones en la ventana
boton_1.grid(row=1, column=0, padx=5, pady=5)
boton_2.grid(row=1, column=1, padx=5, pady=5)
boton_3.grid(row=1, column=2, padx=5, pady=5)
boton_4.grid(row=2, column=0, padx=5, pady=5)
boton_5.grid(row=2, column=1, padx=5, pady=5)
boton_6.grid(row=2, column=2, padx=5, pady=5)
boton_7.grid(row=3, column=0, padx=5, pady=5)
boton_8.grid(row=3, column=1, padx=5, pady=5)
boton_9.grid(row=3, column=2, padx=5, pady=5)
boton_suma.grid(row=1, column=3, padx=5, pady=5)
boton_resta.grid(row=2, column=3, padx=5, pady=5)
boton_multiplicacion.grid(row=3, column=3, padx=5, pady=5)
boton_division.grid(row=4, column=3, padx=5, pady=5)
boton_igual.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
boton_punto.grid(row=4, column=2, padx=5, pady=5)

root.mainloop()
