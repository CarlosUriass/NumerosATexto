# Definición de listas que contienen palabras para representar los números en diferentes rangos
numeros_millones = ["un", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
numeros_centenas = ["cien", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]
numeros_decenas = ["diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
numeros_decenas_adicionales = ["dieci", "veinti", "treinta y", "cuarenta y", "cincuenta y", "sesenta y", "setenta y", "ochenta y", "noventa y"]
numeros_unidades = ["uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
numeros_especiales = ["once", "doce", "trece", "catorce", "quince"]
numeros_millares = ["mil", "dos mil", "tres mil", "cuatro mil", "cinco mil", "seis mil", "siete mil", "ocho mil", "nueve mil", "diez mil"]

def main(millones, centenas_millon, decenas_millon, millares, centenas, decenas, unidades):
    """
    Convierte cada parte del número en palabras, considerando su posición y valor.
    
    Parámetros:
    - millones (int): Número de millones.
    - centenas_millon (int): Número de centenas de millón.
    - decenas_millon (int): Número de decenas de millón.
    - millares (int): Número de millares.
    - centenas (int): Número de centenas.
    - decenas (int): Número de decenas.
    - unidades (int): Número de unidades.
    
    Retorna:
    - texto (str): Representación textual del número.
    """
    texto = ""

    if millones > 0:
        if millones == 1:
            texto += numeros_millones[millones - 1] + " millón "
        else:
            texto += numeros_millones[millones - 1] + " millones "

    if centenas_millon > 0:
        if centenas_millon == 1 and decenas_millon >= 1:
            texto += numeros_centenas[centenas_millon - 1] + "to"
        elif centenas_millon <= 9 and decenas_millon >=1:
            texto += numeros_centenas[centenas_millon - 1]
        elif centenas_millon <= 9 and decenas_millon == 0 and millares == 0:
            texto += numeros_centenas[centenas_millon - 1] + " " + "mil"

    if decenas_millon > 0:
        if decenas_millon == 1 and millares <= 5 and millares != 0:
            texto += " " + numeros_especiales[millares -1] + " mil"
        elif decenas_millon <= 9 and millares == 0:
            texto += " " + numeros_decenas[decenas_millon -1] + " mil"
        elif decenas_millon <= 9 and millares >= 1:
            texto += " " + numeros_decenas_adicionales[decenas_millon - 1] + " " + numeros_unidades[millares - 1] + " mil"

    if decenas_millon == 0 and millares >= 1:
        texto += " " + numeros_millares[millares -1]

    if centenas > 0:
        if centenas == 1 and decenas >= 1:
            texto += " " + numeros_centenas[centenas - 1] + "to"
        elif centenas <= 9 and decenas <= 9:
            texto += " " + numeros_centenas[centenas - 1] 

    if decenas > 0:
        if decenas == 1 and unidades <= 5:
            texto += " " + numeros_especiales[unidades - 1]
        elif decenas <= 9 and unidades == 0:
            texto += " " + numeros_decenas[decenas -1]
        else:
            texto += " " + numeros_decenas_adicionales[decenas - 1]

    if unidades > 0:
        texto += " " + numeros_unidades[unidades -1]

    return texto

def convertir_a_texto(numero):
    """
    Convierte un número entero en su representación textual en español.
    
    Parámetros:
    - numero (str o int): Número a convertir.
    
    Retorna:
    - texto (str): Representación textual del número.
    """
    numero = int(numero)  # Convertir el número a entero

    millones = numero // 1000000
    centenas_millon = (numero % 1000000) // 100000
    decenas_millon = (numero % 100000) // 10000
    millar = (numero % 10000) // 1000
    centenas = (numero % 1000) // 100
    decenas = (numero % 100) // 10
    unidades = (numero % 10)

    return main(millones, centenas_millon, decenas_millon, millar, centenas, decenas, unidades)

def separar_numeros(numero):
    """
    Divide un número dado en su parte entera y su parte decimal, luego convierte ambas partes en palabras.
    
    Parámetros:
    - numero (str): Número a dividir y convertir.
    
    Retorna:
    - texto (str): Representación textual del número.
    """
    for i in range(len(numero)):
        if numero[i] == ".":
            parte_entera = convertir_a_texto(numero[:i])
            parte_decimal = convertir_a_texto(numero[i+1:])
            return parte_entera + " pesos con " + parte_decimal + " centavos"
        
    return convertir_a_texto(numero) + " pesos"

def numero_a_texto(numero):
    """
    Convierte un número, representado como una cadena, en su representación textual en español.
    
    Parámetros:
    - numero (str): Número a convertir.
    
    Retorna:
    - texto (str): Representación textual del número.
    """
    return separar_numeros(numero)


