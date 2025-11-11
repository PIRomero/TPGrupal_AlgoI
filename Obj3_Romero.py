import tkinter as tk
from tkinter import messagebox
import doctest

def cifrar_atbash(mensaje):
    #Cifra el mensaje mensaje asignandole a cada caracter el valor de la letra ubicada en el lado contrario del abecedario y cambiandolo de mayuscula a minuscula y viceversa 
    """
    >>> cifrar_atbash("hola")
    'SLOZ'
    >>> cifrar_atbash("HOLA")
    'sloz'
    >>> cifrar_atbash("xyz")
    'CBA'
    >>> cifrar_atbash("XYZ")
    'cba'
    >>> cifrar_atbash("Año 2025")
    'zML 7974'
    >>> cifrar_atbash("ABC")
    'zyx'
    >>> cifrar_atbash("abc")
    'ZYX'
    >>> cifrar_atbash("Python 3.9.0")
    'kBGSLN 6.0.9'
    >>> cifrar_atbash("Cifrado Atbash")
    'xRUIZWL zGYZHS'
    >>> cifrar_atbash("AaZz")
    'zZaA'
    """
    minusculas = "abcdefghijklmnñopqrstuvwxyz"
    mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

    resultado = []

    for caracter in mensaje:
        if caracter in minusculas:
            nuevo = mayusculas[len(minusculas) - 1 - minusculas.index(caracter)]
            resultado.append(nuevo)
        elif caracter in mayusculas:
            nuevo = minusculas[len(mayusculas) - 1 - mayusculas.index(caracter)]
            resultado.append(nuevo)
        elif '0' <= caracter <= '9':
            nuevo = chr(ord('9') - (ord(caracter) - ord('0')))
            resultado.append(nuevo)
        else:
            resultado.append(caracter)

    return "".join(resultado)

def cifrar_cesar(mensaje, clave):
    #Cifra el mensaje mensaje desplazando cada caracter la cantidad de espacios indicados por la clave en el alfabeto
    """
    >>> cifrar_cesar("hola", 1)
    'ipmb'
    >>> cifrar_cesar("HOLA", 1)
    'IPMB'
    >>> cifrar_cesar("xyz", 3)
    'abc'
    >>> cifrar_cesar("XYZ", 3)
    'ABC'
    >>> cifrar_cesar("Anno 2025", 5)
    'Fsst 7570'
    >>> cifrar_cesar("ABC", -1)
    'ZAB'
    >>> cifrar_cesar("abc", -1)
    'zab'
    >>> cifrar_cesar("Python 3.9.0", 4)
    'Tcxlsr 7.3.4'
    >>> cifrar_cesar("Cifrado Cesar", 0)
    'Cifrado Cesar'
    >>> cifrar_cesar("AaZz", 2)
    'CcBb'
    """

    CANTIDAD_LETRAS = 26
    CANTIDAD_NUMEROS = 10
    resultado = []
    
    for caracter in mensaje:
        if 'a' <= caracter <= 'z':
            nuevo = chr((ord(caracter) - ord('a') + clave) % CANTIDAD_LETRAS + ord('a'))
            resultado.append(nuevo)
        elif 'A' <= caracter <= 'Z':
            nuevo = chr((ord(caracter) - ord('A') + clave) % CANTIDAD_LETRAS + ord('A'))
            resultado.append(nuevo)
        elif  '0' <= caracter <= '9':
            nuevo = chr((ord(caracter) - ord('0') + clave) % CANTIDAD_NUMEROS + ord('0'))
            resultado.append(nuevo)
        else:
            resultado.append(caracter)

    return "".join(resultado)

print(doctest.testmod())

def abrir_ventana_principal():
    #Ventana principal del aplicativo
    ventana_bienvenida.destroy()

    ventana = tk.Tk()
    ventana.title("TP Grupal Parte 1 - Grupo: Romero")
    ventana.geometry("450x350")
    ventana.resizable(False, False)

    tk.Label(ventana, text="Ingrese su mensaje:", font=("Arial", 12)).pack(pady=5)
    entrada_mensaje = tk.Entry(ventana, width=50)
    entrada_mensaje.pack(pady=5)

    tk.Label(ventana, text="Clave (Solo para Cesar):", font=("Arial", 12)).pack(pady=5)
    entrada_clave = tk.Entry(ventana, width=10)
    entrada_clave.pack(pady=5)

    resultado_label = tk.Label(ventana, text="", font=("Arial", 12), wraplength=400)
    resultado_label.pack(pady=15)

    def boton_cifrar_cesar():
        mensaje = entrada_mensaje.get()
        try:
            clave = int(entrada_clave.get())
        except:
            messagebox.showerror("Error", "La clave debe ser un numero entero.")
            return
        resultado_label.config(text=cifrar_cesar(mensaje, clave))

    def boton_descifrar_cesar():
        mensaje = entrada_mensaje.get()
        try:
            clave = int(entrada_clave.get())
        except:
            messagebox.showerror("Error", "La clave debe ser un numero entero.")
            return
        resultado_label.config(text=cifrar_cesar(mensaje, -clave))

    def boton_cifrar_atbash():
        mensaje = entrada_mensaje.get()
        resultado_label.config(text=cifrar_atbash(mensaje))

    def boton_descifrar_atbash():
        mensaje = entrada_mensaje.get()
        resultado_label.config(text=cifrar_atbash(mensaje))

    tk.Button(ventana, text="Cifrar Cesar", width=20, command=boton_cifrar_cesar).pack(pady=3)
    tk.Button(ventana, text="Cifrar Atbash", width=20, command=boton_cifrar_atbash).pack(pady=3)
    tk.Button(ventana, text="Descifrar Cesar", width=20, command=boton_descifrar_cesar).pack(pady=3)
    tk.Button(ventana, text="Descifrar Atbash", width=20, command=boton_descifrar_atbash).pack(pady=3)

    ventana.mainloop()

#Instancia de la ventana
ventana_bienvenida = tk.Tk()
ventana_bienvenida.title("TP Grupal Parte 1 - Grupo: Romero")
ventana_bienvenida.geometry("500x350")
ventana_bienvenida.resizable(False, False)

tk.Label(
    ventana_bienvenida,
    text="Bienvenido a la aplicacion de mensajes secretos del grupo Romero.\n\n"
         "Para continuar presione continuar.",
    font=("Arial", 12), wraplength=450, justify="center"
).pack(pady=20)

tk.Button(ventana_bienvenida, text="Continuar", command=abrir_ventana_principal).pack(pady=10)

tk.Label(ventana_bienvenida, text="Construida por:", font=("Arial", 12)).pack(pady=10)
tk.Label(ventana_bienvenida, text="Pablo Ivan Romero", font=("Arial", 11)).pack()

ventana_bienvenida.mainloop()
