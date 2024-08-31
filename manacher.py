def manacher(s):
    # Transformación de la cadena
    T = '#' + '#'.join(s) + '#'
    n = len(T)
    P = [0] * n
    C = 0  # Centro actual del palíndromo
    R = 0  # Borde derecho del palíndromo actual

    for i in range(n):
        mirr = 2 * C - i  # Posición espejo de i respecto al centro C

        if i < R:
            P[i] = min(R - i, P[mirr])

        # Intenta expandir el palíndromo centrado en i
        while i + P[i] + 1 < n and i - P[i] - 1 >= 0 and T[i + P[i] + 1] == T[i - P[i] - 1]:
            P[i] += 1

        # Si el palíndromo se expande más allá de R, actualiza C y R
        if i + P[i] > R:
            C = i
            R = i + P[i]

    # El vector P contiene los radios de los palíndromos centrados en cada posición de T
    return P

# Ejemplo de uso
s = "abacabad"
P = manacher(s)
print("Vector de radios de palíndromos:", P)

# Opcional: Mostrar los palíndromos basados en P
palindromos = []
for i in range(1, len(P) - 1):
    longitud = P[i]
    if longitud > 0:
        start = (i - longitud) // 2
        palindromos.append(s[start:start + longitud])

print("Palíndromos encontrados:", palindromos)
