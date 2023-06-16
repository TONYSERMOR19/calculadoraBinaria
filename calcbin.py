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
