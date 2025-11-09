import doctest

def cifrado_cesar(palabra, clave):
    #Cifra la palabra desplazando cada caracter la cantidad de espacios indicados por la clave
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

    resultado = []

    for caracter in palabra:
        if 'a' <= caracter <= 'z':
            nuevo = chr((ord(caracter) - ord('a') + clave) % 26 + ord('a'))
            resultado.append(nuevo)
        elif 'A' <= caracter <= 'Z':
            nuevo = chr((ord(caracter) - ord('A') + clave) % 26 + ord('A'))
            resultado.append(nuevo)
        elif  '0' <= caracter <= '9':
            nuevo = chr((ord(caracter) - ord('0') + clave) % 10 + ord('0'))
            resultado.append(nuevo)
        else:
            resultado.append(caracter)

    return "".join(resultado)

print(doctest.testmod())
