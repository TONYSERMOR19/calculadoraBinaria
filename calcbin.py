def suma_binaria(binario1, binario2):
    decimal1 = binario_decimal(binario1)
    decimal2 = binario_decimal(binario2)
    suma_decimal = decimal1 + decimal2
    resultado_binario = decimal_binario(suma_decimal)
    return resultado_binario