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

print(doctest.testmod())
