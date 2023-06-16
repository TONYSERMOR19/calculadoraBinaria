
def resta_binaria(binario1, binario2):
    decimal1 = binario_decimal(binario1)
    decimal2 = binario_decimal(binario2)
    resta_decimal = decimal1 - decimal2
    resultado_binario = decimal_binario(resta_decimal)
    return resultado_binario

def multiplicacion_binaria(binario1, binario2):
    decimal1 = binario_decimal(binario1)
    decimal2 = binario_decimal(binario2)
    multiplicacion_decimal = decimal1 * decimal2
    resultado_binario = decimal_binario(multiplicacion_decimal)
    return resultado_binario

def binario_decimal(numero):
    decimal = 0
    posicion = len(numero) - 1
    for digito in numero:
        decimal += int(digito) * (2 ** posicion)
        posicion -= 1
    return decimal

def decimal_binario(numero):
    binario = ""
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero //= 2
    return binario

