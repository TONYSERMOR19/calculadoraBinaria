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