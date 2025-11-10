import tkinter as tk
from tkinter import messagebox
import doctest

def cifrar_atbash(mensaje):
    #Cifra el mensaje mensaje asignandole a cada caracter el valor de la letra ubicada en el lado contrario del abecedario y cambiandolo de mayuscula a minuscula y viceversa 
    """
    >>> cifrado_atbash("hola")
    'SLOZ'
    >>> cifrado_atbash("HOLA")
    'sloz'
    >>> cifrado_atbash("xyz")
    'CBA'
    >>> cifrado_atbash("XYZ")
    'cba'
    >>> cifrado_atbash("Año 2025")
    'zML 7974'
    >>> cifrado_atbash("ABC")
    'zyx'
    >>> cifrado_atbash("abc")
    'ZYX'
    >>> cifrado_atbash("Python 3.9.0")
    'kBGSLN 6.0.9'
    >>> cifrado_atbash("Cifrado Atbash")
    'xRUIZWL zGYZHS'
    >>> cifrado_atbash("AaZz")
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
    >>> cifrado_cesar("hola", 1)
    'ipmb'
    >>> cifrado_cesar("HOLA", 1)
    'IPMB'
    >>> cifrado_cesar("xyz", 3)
    'abc'
    >>> cifrado_cesar("XYZ", 3)
    'ABC'
    >>> cifrado_cesar("Anno 2025", 5)
    'Fsst 7570'
    >>> cifrado_cesar("ABC", -1)
    'ZAB'
    >>> cifrado_cesar("abc", -1)
    'zab'
    >>> cifrado_cesar("Python 3.9.0", 4)
    'Tcxlsr 7.3.4'
    >>> cifrado_cesar("Cifrado Cesar", 0)
    'Cifrado Cesar'
    >>> cifrado_cesar("AaZz", 2)
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



def abrir_ventana_principal():
    ventana_bienvenida.destroy()

    ventana = tk.Tk()
    ventana.title("TP Grupal Parte 1 - Grupo: Romero")
    ventana.geometry("450x350")
    ventana.resizable(False, False)

    tk.Label(ventana, text="Ingrese su mensaje:", font=("Arial", 12)).pack(pady=5)
    entrada_mensaje = tk.Entry(ventana, width=50)
    entrada_mensaje.pack(pady=5)

    tk.Label(ventana, text="Clave (Sólo para César):", font=("Arial", 12)).pack(pady=5)
    entrada_clave = tk.Entry(ventana, width=10)
    entrada_clave.pack(pady=5)

    resultado_label = tk.Label(ventana, text="", font=("Arial", 12), wraplength=400)
    resultado_label.pack(pady=15)

    def boton_cifrar_cesar():
        mensaje = entrada_mensaje.get()
        try:
            clave = int(entrada_clave.get())
        except:
            messagebox.showerror("Error", "La clave debe ser un número entero.")
            return
        resultado_label.config(text=cifrar_cesar(mensaje, clave))

    def boton_descifrar_cesar():
        mensaje = entrada_mensaje.get()
        try:
            clave = int(entrada_clave.get())
        except:
            messagebox.showerror("Error", "La clave debe ser un número entero.")
            return
        resultado_label.config(text=cifrar_cesar(mensaje, -clave))

    def boton_cifrar_atbash():
        mensaje = entrada_mensaje.get()
        resultado_label.config(text=cifrar_atbash(mensaje))

    def boton_descifrar_atbash():
        mensaje = entrada_mensaje.get()
        resultado_label.config(text=cifrar_atbash(mensaje))

    tk.Button(ventana, text="Cifrar César", width=20, command=boton_cifrar_cesar).pack(pady=3)
    tk.Button(ventana, text="Cifrar Atbash", width=20, command=boton_cifrar_atbash).pack(pady=3)
    tk.Button(ventana, text="Descifrar César", width=20, command=boton_descifrar_cesar).pack(pady=3)
    tk.Button(ventana, text="Descifrar Atbash", width=20, command=boton_descifrar_atbash).pack(pady=3)

    ventana.mainloop()

ventana_bienvenida = tk.Tk()
ventana_bienvenida.title("TP Grupal Parte 1 - Grupo: Romero")
ventana_bienvenida.geometry("500x350")
ventana_bienvenida.resizable(False, False)

tk.Label(
    ventana_bienvenida,
    text="Bienvenido a la aplicación de mensajes secretos del grupo Romero.\n\n"
         "Para continuar presione continuar, de lo contrario cierre la ventana.",
    font=("Arial", 12), wraplength=450, justify="center"
).pack(pady=20)

tk.Button(ventana_bienvenida, text="Continuar", command=abrir_ventana_principal).pack(pady=10)

tk.Label(ventana_bienvenida, text="Construída por:", font=("Arial", 12)).pack(pady=10)
tk.Label(ventana_bienvenida, text="Pablo Ivan Romero", font=("Arial", 11)).pack()

ventana_bienvenida.mainloop()
