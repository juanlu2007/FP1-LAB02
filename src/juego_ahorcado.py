import random

def elige_palabra(fichero="palabras.txt"):
    """
    Devuelve una palabra aleatoria tomada de un fichero de texto.

    Parámetros:
        fichero: ruta al archivo que contiene las palabras (una por línea).

    Devuelve:
        Una palabra (str) elegida al azar del fichero.
    """
    with open(fichero, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    # Quitar saltos de línea y espacios
    palabras = [linea.strip() for linea in lineas if linea.strip() != ""]
    cadena = random.choice(palabras)
    return cadena

def normalizar(cadena):
    """
    Normaliza una cadena de texto realizando las siguientes operaciones:
        - convierte a minúsculas
        - quita espacios en blanco al principio y al final
        - elimina acentos y diéresis        
    
    Parámetros:
      cadena: cadena de texto que hay que sanear
    
    Devuelve:
      Cadena de texto con la palabra normalizada
    """
    cadena = cadena.lower()
    cadena = cadena.strip()
    cadena = cadena.replace("á","a")
    cadena = cadena.replace("é","e")
    cadena = cadena.replace("í","i")
    cadena = cadena.replace("ó","o")
    cadena = cadena.replace("ú","u")
    cadena = cadena.replace("ü","u")
    return cadena

def ocultar(cadena, letras_usadas=""):
    '''Devuelve una cadena de texto con la palabra enmascarada. 
    Las letras que no están en letras_usadas se muestran como guiones bajos (_).

    Parámetros:
    - palabra_secreta: cadena de texto con la palabra que se debe enmascarar
    - letras_usadas: cadena de texto con las letras que se deben mostrar (por defecto cadena vacía)

    Devuelve:
      Cadena de texto con la palabra enmascarada
    '''
    palabra_enmascarada = ""
    for letra in cadena:
        if letra in letras_usadas:
            palabra_enmascarada += letra
        else:
            palabra_enmascarada += "_"
    return palabra_enmascarada

def ha_ganado(palabra_enmascarada):
    '''Devuelve True si el jugador ha ganado (es decir, si no quedan letras por descubrir en la palabra enmascarada).'''
    if "_" in palabra_enmascarada:
        return False
    else:
        return True

def mostrar_estado(palabra_enmascarada, letras_usadas, intentos_restantes):
    print("Estado:", " ".join(palabra_enmascarada))
    print("Letras usadas:", letras_usadas if letras_usadas else "Ninguna")
    print("Intentos restantes:", intentos_restantes)

def pedir_letra(letras_usadas):
    letra = input("Introduce una letra: ").lower()
    while not letra.isalpha():  # solo letras
        print("Solo son válidas las letras")
        letra = input("Introduce una letra: ").lower()
    while len(letra) > 1:
        print("Solo una letra")
        letra = input("Introduce una letra: ").lower()
    while letra in letras_usadas:
        print("Esa letra ya la has dicho")
        letra = input("Introduce una letra: ").lower()
    return letra

def jugar(cadena, intentos_restantes=6):
    cadena = normalizar(cadena)
    letras_usadas = ""
    palabra_enmascarada = ocultar(cadena, letras_usadas)
    while intentos_restantes > 0 and not ha_ganado(palabra_enmascarada):
        mostrar_estado(palabra_enmascarada, letras_usadas, intentos_restantes)
        letra = pedir_letra(letras_usadas)
        letras_usadas += letra 
        if letra not in cadena:
            print("Esta letra no está en la palabra")
            intentos_restantes -= 1
        else:
            print("¡Has acertado la letra!")
        # ✅ CORREGIDO: ahora sí usa las letras acumuladas
        palabra_enmascarada = ocultar(cadena, letras_usadas)
    if ha_ganado(palabra_enmascarada):
        print("¡Has ganado!")
    else:
        print("Has perdido, la palabra era", cadena)

# Programa principal
cadena = elige_palabra("palabras.txt")
jugar(cadena)