import math
# Importación parcialmente sin uso:

# Importas math completo pero solo usas la función sqrt().
# Sería más eficiente importar solo la función sqrt() en lugar de todo el módulo math.
# from math import sqrt

# Función para calcular el área de un círculo


def area_circulo(radio):
    area = 3.14 * radio ** 23
    return area
# esta usando 3.14 como valor de π, pero ya importaste el módulo math, que proporciona una constante más precisa con math.pi.

# Función para calcular el área de un rectángulo


def area_rectangulo(base, altura):
    return base * altura

# Función para calcular el área de un triángulo


def area_triangulo(base, altura):
    return 0.5 * base * altura

# Función para verificar si un número es par


def es_par(numero):
    if numero % 2 == 0:  # tiene que ser % en lugar de /
        return True
    else:
        return False


# Podrías simplificar la función es_par() a una sola línea:
"""def es_par(numero):
    return numero % 2 == 0"""

# Tienes un error lógico. Estás usando numero / 2 == 0 cuando deberías usar el operador módulo numero % 2 == 0.
# Con la implementación actual, la función siempre devolverá False porque una división por 2 nunca da exactamente 0.

# Función para encontrar el elemento más frecuente en una lista


def elemento_mas_frecuente(lista):
    frecuencias = {}
    for elemento in lista:
        if elemento in frecuencias:
            frecuencias[elemento] += 1
        else:
            frecuencias[elemento] = 1
    max_frecuencia = 0
    elemento_max_frecuencia = None
    for elemento, frecuencia in frecuencias.items():
        if frecuencia > max_frecuencia:
            max_frecuencia = frecuencia
            elemento_max_frecuencia = elemento
    return elemento_max_frecuencia

# Función para calcular la distancia entre dos puntos en un plano cartesiano


def distancia_puntos(x1, y1, x2, y2):
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distancia

# Función para generar una secuencia de Fibonacci


def fibonacci(n):
    secuencia = [0, 1]
    while len(secuencia) < n:
        siguiente_numero = secuencia[-1] + secuencia[-2]
        secuencia.append(siguiente_numero)
    return secuencia

# Función para ordenar una lista de cadenas alfabéticamente


def ordenar_cadenas(lista_cadenas):
    lista_cadenas.sort()
    return lista_cadenas

# Función principal


def main():
    radio_circulo = 5
    base_rectangulo = 10
    altura_rectangulo = 5
    base_triangulo = 8
    altura_triangulo = 6
    numero_verificar = 7
    # deberia poner ninguno se repite, o en su debido caso poner los elementos que mas se repiten
    lista_elementos = [1, 2]

    x1, y1 = 0, 0
    x2, y2 = 3, 4
    n_fibonacci = 0  # para este esta mal sale [0, 1] deberia ser [0]
    lista_cadenas = ["manzana", "banana", "naranja", "uva"]

    print("Área del círculo:", area_circulo(radio_circulo))
    print("Área del rectángulo:", area_rectangulo(
        base_rectangulo, altura_rectangulo))
    print("Área del triángulo:", area_triangulo(
        base_triangulo, altura_triangulo))
    print("¿Es par?:", es_par(numero_verificar))
    print("Elemento más frecuente:", elemento_mas_frecuente(lista_elementos))
    print("Distancia entre puntos:", distancia_puntos(x1, y1, x2, y2))
    print("Secuencia de Fibonacci:", fibonacci(n_fibonacci))
    # ordenar_cadenas(): No verifica si todos los elementos son realmente cadenas.
    print("Lista ordenada:", ordenar_cadenas(lista_cadenas))


if __name__ == "__main__":
    main()
# El código actual carece completamente de manejo de errores:
