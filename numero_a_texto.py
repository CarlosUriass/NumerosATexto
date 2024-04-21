def numeros_a_texto(numero):
    numeros_unidades = ["uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    numeros_decenas = ["diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    numeros_centenas = ["cien", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]
    especiales = ["once", "doce", "trece", "catorce", "quince"]
    numeros_decenas_adicionales = ["dieci", "veinti", "treinta y ", "cuarenta y ", "cincuenta y ", "sesenta y ", "setenta y ", "ochenta y ", "noventa y "]
   
    numero = str(numero)

    unidades = int(numero[-1])
    decenas = int(numero[-2])
    centenas = int(numero[-3])

    texto = ""

    if centenas > 0:
        if centenas == 1 and decenas >= 1:
            texto += numeros_centenas[centenas - 1] + "to " 
        elif centenas <= 9 and centenas >= 1:
            texto += numeros_centenas[centenas - 1] + " "

    if decenas > 0:
        if decenas == 1 and unidades <= 5:
            texto += especiales[unidades - 1] 
        elif decenas == 1 and unidades > 5:
            texto += numeros_decenas_adicionales[decenas - 1] 
        else:
            texto += numeros_decenas_adicionales[decenas - 1]

    if unidades > 0:
        if decenas != 1:
            texto += numeros_unidades[unidades - 1] 

    return texto


def separar_en_tres(numero):
    unidades = ""
    millares = ""
    millones = ""

    numero = numero.zfill(9)

    if int(numero[:3]):
        millones = numeros_a_texto(numero[:3]) + " millones"
        if numero[:3] == "001":
            millones = "un millón"

    if int(numero[3:6]):
        millares = numeros_a_texto(numero[3:6]) + " mil"

    if int(numero[6:9]):
        unidades = numeros_a_texto(numero[6:9]) 

    if millones == "" and millares == "" and unidades == "un":
        unidades = "un"

    return millones + " " + millares + " " + unidades


def isZero(numero):
    numero = int(numero)
    texto = ""

    if numero == 0:
        texto = " cero"
        return texto
    else:
        numero = str(numero)
        return separar_en_tres(numero)
    
def addzero(centavos):
    zero = "0"
    if len(centavos) == 1:
        centavos += zero
        return isZero(centavos)
    else:
        return isZero(centavos) 


def separar_numeros(numero):
  
    for i in range(len(numero)):
        if numero[i] == ".":
            parte_entera = isZero(numero[:i])
            parte_decimal = addzero(numero[i+1:])
            return parte_entera + " pesos con" + parte_decimal + " centavos"
        
    return isZero(numero) + " pesos"


def num_txt(cifra):
    return separar_numeros(cifra)