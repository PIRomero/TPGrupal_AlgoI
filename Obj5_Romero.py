import tkinter as tk
from tkinter import messagebox, ttk
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

CANTIDAD_LETRAS = 26
CANTIDAD_NUMEROS = 10

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

def validar_usuario(usuario):
    # Hace las validaciones del usuario
    valido = True
    n = len(usuario)
    if n < 5 or n > 15:
        valido =  False

    c = 0
    while (c < len(usuario) and valido):
        caracter = usuario[c]
        # alfanumericos y '_', '-', '.'
        if not(caracter.isalnum() or caracter == '_' or caracter == '-' or caracter == '.'):
            valido = False
        c += 1
        
    return valido

def validar_clave(clave):
    # Hace las validacion de la clave    
    n = len(clave)
    if n < 4 or n > 8:
        return False

    has_upper = False
    has_lower = False
    has_digito = False
    has_simbolo = False
    simbolos = "_-#*"

    valido = True
    i = 0
    while (i < len(clave) and valido):
        c = clave[i]
        if c.isupper():
            has_upper = True
        elif c.islower():
            has_lower = True
        elif c.isdigit():
            has_digito = True
        elif c in simbolos:
            has_simbolo = True
        else:
            valido = False  # caracter no permitido

        if i > 0 and clave[i] == clave[i-1]:
            valido = False  # repetido adyacente
        i += 1
    if (not(has_upper and has_lower and has_digito and has_simbolo)):
        valido = False
        
    return valido

def existe_archivo(ruta):
    # Devuelve todos los usuarios guardaros
    try:
        f = open(ruta, "r", encoding="utf-8")
        f.close()
        return True
    except:
        return False

PREGUNTAS_FILE = "preguntas.csv"
USUARIOS_FILE = "usuarios.csv"
RECUP_FILE = "recuperacion.csv"

def asegurar_preguntas():
    # Devuelve todos los usuarios guardaros
    if existe_archivo(PREGUNTAS_FILE):
        return
    preguntas = [
        (1, "Apellido de su abuela materna"),
        (2, "Nombre de tu mascota"),
        (3, "Nombre de tu mejor amigo/amiga"),
        (4, "Cantante preferido"),
        (5, "Ciudad preferida"),
        (6, "Comida favorita"),
        (7, "Color favorito"),
        (8, "Nombre de tu primer profesor"),
        (9, "Deporte favorito"),
        (10, "Nombre de tu pelicula favorita")
    ]
    try:
        f = open(PREGUNTAS_FILE, "w", encoding="utf-8")
        for pid, texto in preguntas:
            f.write(str(pid) + "," + texto.replace("\n"," ") + "\n")
        f.close()
    except Exception as e:
        print("Error creando preguntas:", e)

def leer_preguntas():
    # Devuelve todos los usuarios guardaros
    asegurar_preguntas()
    preguntas = []
    try:
        f = open(PREGUNTAS_FILE, "r", encoding="utf-8")
        for linea in f:
            linea = linea.strip()
            if linea == "":
                continue
            partes = linea.split(",", 1)
            if len(partes) == 2:
                preguntas.append((partes[0], partes[1]))
        f.close()
    except:
        pass
    return preguntas

def leer_usuarios():
    # Devuelve todos los usuarios guardaros
    users = {}
    if not existe_archivo(USUARIOS_FILE):
        return users
    try:
        f = open(USUARIOS_FILE, "r", encoding="utf-8")
        for linea in f:
            linea = linea.strip()
            if linea == "":
                continue
            partes = linea.split(",", 4)
            # Id_usuario,clave_usuario,id_pregunta,respuesta_recuperacion,intentos_recuperacion
            if len(partes) < 5:
                continue
            idu = partes[0]
            clave = partes[1]
            id_preg = partes[2]
            resp = partes[3]
            try:
                intentos = int(partes[4])
            except:
                intentos = 0
            users[idu] = {
                "clave": clave,
                "id_preg": id_preg,
                "resp": resp,
                "intentos_recuperacion": intentos
            }
        f.close()
    except:
        pass
    return users

def guardar_usuario(users):
    # Guarda el nuevo usuario
    try:
        f = open(USUARIOS_FILE, "w", encoding="utf-8")
        for idu, datos in users.items():
            linea = idu + "," + datos["clave"] + "," + datos["id_preg"] + "," + datos["resp"] + "," + str(datos.get("intentos_recuperacion",0))
            f.write(linea + "\n")
        f.close()
    except Exception as e:
        print("Error guardando usuarios:", e)

def registrar_intento_recuperacion(usuario_id):
    # Guarda usuario y numero de intento en un csv si la respuesta fue incorrecta
    try:
        f = open(RECUP_FILE, "a", encoding="utf-8")
        f.write(usuario_id + "\n")
        f.close()
    except:
        pass

def guardar_mensaje(destinatario, remitente, cifrado, mensaje_cifrado):
    # Guarda el mensaje cifrado
    try:
        with open("mensajes.csv", "a", encoding="utf-8") as f:
            f.write(destinatario + "," + remitente + "," + cifrado + "," + mensaje_cifrado + "\n")
    except:
        ventana_error = Toplevel()
        ventana_error.title("Error")
        Label(ventana_error, text="No se pudo guardar el mensaje.").pack()

def abrir_ventana_principal():
    # Interfaz principal del programa
    ventana = tk.Toplevel()
    ventana.title("TP Grupal Parte 2 - Grupo: Romero")
    ventana.geometry("480x380")
    ventana.resizable(False, False)

    tk.Label(ventana, text="Ingrese su mensaje:", font=("Arial", 12)).pack(pady=5)
    entrada_mensaje = tk.Entry(ventana, width=60)
    entrada_mensaje.pack(pady=5)

    tk.Label(ventana, text="Clave (Solo para Cesar):", font=("Arial", 12)).pack(pady=5)
    entrada_clave = tk.Entry(ventana, width=10)
    entrada_clave.pack(pady=5)

    resultado_label = tk.Label(ventana, text="", font=("Arial", 12), wraplength=440, justify='left')
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

    btn_frame = tk.Frame(ventana)
    btn_frame.pack(pady=5)

    tk.Button(btn_frame, text="Cifrar Cesar", width=18, command=boton_cifrar_cesar).grid(row=0, column=0, padx=5, pady=3)
    tk.Button(btn_frame, text="Cifrar Atbash", width=18, command=boton_cifrar_atbash).grid(row=0, column=1, padx=5, pady=3)
    tk.Button(btn_frame, text="Descifrar Cesar", width=18, command=boton_descifrar_cesar).grid(row=1, column=0, padx=5, pady=3)
    tk.Button(btn_frame, text="Descifrar Atbash", width=18, command=boton_descifrar_atbash).grid(row=1, column=1, padx=5, pady=3)
    tk.Button(btn_frame, text="Enviar mensaje cifrado César", width=18, command=enviar_cifrado_cesar).grid(row=2, column=0, padx=5, pady=3)
    tk.Button(btn_frame, text="Enviar mensaje cifrado Atbash", width=18, command=enviar_cifrado_atbash).grid(row=2, column=1, padx=5, pady=3)

def enviar_cifrado_cesar():
    # Ventana para enviar el mensaje cifrado en Cesar
    ventana_envio = Toplevel()
    ventana_envio.title("Enviar mensaje cifrado César")

    Label(ventana_envio, text="Destinatario (* para todos):").pack()
    entrada_destinatario = Entry(ventana_envio)
    entrada_destinatario.pack()

    Label(ventana_envio, text="Clave de cifrado:").pack()
    entrada_clave = Entry(ventana_envio)
    entrada_clave.pack()

    Label(ventana_envio, text="Mensaje a cifrar:").pack()
    entrada_mensaje = Entry(ventana_envio, width=40)
    entrada_mensaje.pack()

    def confirmar_envio():
        destinatario = entrada_destinatario.get().strip()
        clave = entrada_clave.get().strip()
        mensaje = entrada_mensaje.get().strip()

        if destinatario == "":
            Label(ventana_envio, text="Debe ingresar un destinatario.", fg="red").pack()
            return

        if not (destinatario == "*" or destinatario in leer_usuarios()):
            Label(ventana_envio, text="Destinatario Inexistente", fg="red").pack()
            return

        if not clave.isdigit():
            Label(ventana_envio, text="La clave debe ser numérica.", fg="red").pack()
            return

        clave = int(clave)
        mensaje_cifrado = cifrado_cesar(mensaje, clave)

        guardar_mensaje(destinatario, usuario_actual, f"C{clave}", mensaje_cifrado)
        Label(ventana_envio, text="Mensaje Enviado", fg="green").pack()

    Button(ventana_envio, text="Enviar", command=confirmar_envio).pack(pady=5)

def enviar_cifrado_atbash():
    # Ventana para enviar el mensaje cifrado en atbash
    ventana_envio = Toplevel()
    ventana_envio.title("Enviar mensaje cifrado Atbash")

    Label(ventana_envio, text="Destinatario (* para todos):").pack()
    entrada_destinatario = Entry(ventana_envio)
    entrada_destinatario.pack()

    Label(ventana_envio, text="Mensaje a cifrar:").pack()
    entrada_mensaje = Entry(ventana_envio, width=40)
    entrada_mensaje.pack()

    def confirmar_envio():
        destinatario = entrada_destinatario.get().strip()
        mensaje = entrada_mensaje.get().strip()

        if destinatario == "":
            Label(ventana_envio, text="Debe ingresar un destinatario.", fg="red").pack()
            return

        if not (destinatario == "*" or destinatario in leer_usuarios()):
            Label(ventana_envio, text="Destinatario Inexistente", fg="red").pack()
            return

        mensaje_cifrado = cifrado_atbash(mensaje)

        guardar_mensaje(destinatario, usuario_actual, "A", mensaje_cifrado)
        Label(ventana_envio, text="Mensaje Enviado", fg="green").pack()

    Button(ventana_envio, text="Enviar", command=confirmar_envio).pack(pady=5)
    
def ventana_crear_usuario(parent):
    # Ventana crear usuario
    win = tk.Toplevel(parent)
    win.title("Crear Usuario")
    win.geometry("480x440")
    win.resizable(False, False)

    tk.Label(win, text="Crear nuevo usuario", font=("Arial", 14)).pack(pady=8)

    frame = tk.Frame(win)
    frame.pack(pady=5)

    tk.Label(frame, text="Identificador:").grid(row=0, column=0, sticky='e')
    entry_id = tk.Entry(frame, width=32)
    entry_id.grid(row=0, column=1, pady=3)

    tk.Label(frame, text="Clave:").grid(row=1, column=0, sticky='e')
    entry_clave = tk.Entry(frame, width=32, show="*")
    entry_clave.grid(row=1, column=1, pady=3)

    tk.Label(frame, text="Repetir clave:").grid(row=2, column=0, sticky='e')
    entry_clave2 = tk.Entry(frame, width=32, show="*")
    entry_clave2.grid(row=2, column=1, pady=3)

    tk.Label(frame, text="Pregunta de recuperacion:").grid(row=3, column=0, sticky='e')
    preguntas = leer_preguntas()
    opciones = [pid + ". " + texto for pid, texto in preguntas]
    var_preg = tk.StringVar(win)
    if len(opciones) > 0:
        var_preg.set(opciones[0])
    om = ttk.Combobox(frame, values=opciones, state="readonly", width=34, textvariable=var_preg)
    om.grid(row=3, column=1, pady=3)

    tk.Label(frame, text="Respuesta:").grid(row=4, column=0, sticky='e')
    entry_resp = tk.Entry(frame, width=32)
    entry_resp.grid(row=4, column=1, pady=3)

    def registrar():
        idu = entry_id.get().strip()
        clave = entry_clave.get()
        clave2 = entry_clave2.get()
        resp = entry_resp.get().strip()
        if not validar_usuario(idu):
            messagebox.showerror("Error", "Identificador invalido.\nDebe tener 5-15 caracteres y solo letras, numeros, '_' '-' '.'.")
            return
        if clave != clave2:
            messagebox.showerror("Error", "Las claves no coinciden.")
            return
        if not validar_clave(clave):
            messagebox.showerror("Error", "Clave invalida.\nLongitud 4-8, al menos 1 mayuscula, 1 minuscula, 1 numero, 1 de los siguientes caracteres: _ - # *, y no debe tener caracteres adyacentes repetidos.")
            return
        if resp == "":
            messagebox.showerror("Error", "Debe ingresar una respuesta para la pregunta de recuperacion.")
            return

        users = leer_usuarios()
        if idu in users:
            messagebox.showwarning("Identificador en uso", "Identificador en uso")
            return

        # obtener id pregunta seleccionada
        sel = var_preg.get()
        if sel == "":
            messagebox.showerror("Error", "Seleccione una pregunta.")
            return
        id_preg = sel.split(".",1)[0]

        users[idu] = {
            "clave": clave,
            "id_preg": id_preg,
            "resp": resp,
            "intentos_recuperacion": 0
        }
        guardar_usuario(users)
        messagebox.showinfo("Registrado", "Usuario registrado correctamente.")
        win.destroy()

    tk.Button(win, text="Registrar", width=20, command=registrar).pack(pady=12)
    tk.Button(win, text="Cancelar", width=12, command=win.destroy).pack()

def ventana_ingreso_usuario(parent):
    # Ventana ingreso usuario
    win = tk.Toplevel(parent)
    win.title("Identificacion para acceso")
    win.geometry("420x300")
    win.resizable(False, False)

    tk.Label(win, text="Ingrese sus credenciales", font=("Arial", 13)).pack(pady=8)

    frm = tk.Frame(win)
    frm.pack(pady=5)

    tk.Label(frm, text="Usuario:").grid(row=0, column=0, sticky='e')
    entry_user = tk.Entry(frm, width=30)
    entry_user.grid(row=0, column=1, pady=3)

    tk.Label(frm, text="Clave:").grid(row=1, column=0, sticky='e')
    entry_pass = tk.Entry(frm, width=30, show="*")
    entry_pass.grid(row=1, column=1, pady=3)

    lbl_msg = tk.Label(win, text="", fg="red", wraplength=380, justify='center')
    lbl_msg.pack(pady=6)

    def intentar_ingresar():
        usuario = entry_user.get().strip()
        clave = entry_pass.get()
        users = leer_usuarios()
        
        if usuario not in users:
            lbl_msg.config(text="Identificador inexistente o clave erronea\nSi no se encuentra registrado debe registrarse previamente o si olvidaste la clave presiona el boton recuperar clave")
            return
        datos = users[usuario]
        if datos.get("intentos_recuperacion",0) >= 3:
            messagebox.showwarning("Usuario bloqueado", "Usuario bloqueado")
            return
        if clave != datos["clave"]:
            lbl_msg.config(text="Identificador inexistente o clave erronea\nSi no se encuentra registrado debe registrarse previamente o si olvidaste la clave presiona el boton recuperar clave")
            return

        global usuario_actual
        usuario_actual = usuario
        messagebox.showinfo("Bienvenido", "Bienvenido " + usuario)
        win.destroy()
        abrir_ventana_principal()

    def recuperar_clave():
        usuario = entry_user.get().strip()
        users = leer_usuarios()
        if usuario not in users:
            messagebox.showerror("Error", "Identificador inexistente")
            return
        datos = users[usuario]
        if datos.get("intentos_recuperacion",0) >= 3:
            messagebox.showwarning("Usuario bloqueado", "Usuario bloqueado")
            return

        win_rec = tk.Toplevel(win)
        win_rec.title("Recuperacion Clave")
        win_rec.geometry("420x240")
        win_rec.resizable(False, False)

        id_preg = datos.get("id_preg", "")
        preguntas = leer_preguntas()
        texto_preg = "Pregunta no encontrada"
        for pid,txt in preguntas:
            if pid == id_preg:
                texto_preg = txt
                break

        tk.Label(win_rec, text="Recuperacion de clave", font=("Arial", 13)).pack(pady=6)
        tk.Label(win_rec, text="Pregunta: " + texto_preg, wraplength=380, justify='left').pack(pady=4)
        tk.Label(win_rec, text="Respuesta:").pack()
        entry_resp = tk.Entry(win_rec, width=40)
        entry_resp.pack(pady=6)

        def confirmar_respuesta():
            resp = entry_resp.get().strip()
            nonlocal datos, users
            if resp == datos.get("resp",""):
                messagebox.showinfo("Clave recuperada", "La clave registrada es: " + datos.get("clave",""))
                datos["intentos_recuperacion"] = 0
                users[usuario] = datos
                guardar_usuario(users)
                win_rec.destroy()
            else:
                datos["intentos_recuperacion"] = datos.get("intentos_recuperacion",0) + 1
                users[usuario] = datos
                guardar_usuario(users)
                registrar_intento_recuperacion(usuario)
                if datos["intentos_recuperacion"] >= 3:
                    messagebox.showwarning("Usuario bloqueado", "Respuesta incorrecta. Usuario bloqueado.")
                else:
                    messagebox.showerror("Respuesta incorrecta", "Respuesta incorrecta. Intentos fallidos: " + str(datos["intentos_recuperacion"]))

        tk.Button(win_rec, text="Confirmar", width=16, command=confirmar_respuesta).pack(pady=6)
        tk.Button(win_rec, text="Cerrar", width=12, command=win_rec.destroy).pack()

    tk.Button(win, text="Ingresar", width=14, command=intentar_ingresar).pack(pady=6)
    tk.Button(win, text="Recuperar clave", width=14, command=recuperar_clave).pack()
    tk.Button(win, text="Cerrar", width=12, command=win.destroy).pack(pady=6)

def crear_ventana_bienvenida():
    # Ventana de menu principal
    asegurar_preguntas()
    root = tk.Tk()
    root.title("TP Grupal Parte 1 - Grupo: Romero")
    root.geometry("560x380")
    root.resizable(False, False)

    tk.Label(
        root,
        text="Bienvenido a la aplicacion de mensajes secretos del grupo Romero.\n\n"
             "Para continuar elija una opcion.",
        font=("Arial", 12), wraplength=520, justify="center"
    ).pack(pady=14)

    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=6)

    tk.Button(btn_frame, text="Crear Usuario", width=18, command=lambda: ventana_crear_usuario(root)).grid(row=0, column=0, padx=8)
    tk.Button(btn_frame, text="Ingreso Usuario", width=18, command=lambda: ventana_ingreso_usuario(root)).grid(row=0, column=1, padx=8)

    tk.Label(root, text="Construida por:", font=("Arial", 12)).pack(pady=12)
    tk.Label(root, text="Pablo Ivan Romero", font=("Arial", 11)).pack()

    return root

if __name__ == "__main__":
    asegurar_preguntas()
    app = crear_ventana_bienvenida()
    app.mainloop()
