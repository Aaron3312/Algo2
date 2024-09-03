def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:  # Se añade encoding='utf-8' para manejar caracteres especiales
        return file.read()

def prefix_search(pattern, m, store_prefx):
    length = 0
    store_prefx[0] = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            store_prefx[i] = length
        else:
            if length != 0:
                length = store_prefx[length - 1]
                i -= 1
            else:
                store_prefx[i] = 0
        i += 1

def pattern_search(orgn_string, patt, loc_array):
    n = len(orgn_string)
    m = len(patt)
    i = j = location = 0
    prefix_array = [0] * m

    prefix_search(patt, m, prefix_array)

    while i < n:
        if orgn_string[i] == patt[j]:
            i += 1
            j += 1
        if j == m:
            loc_array[location] = i - j
            location += 1
            j = prefix_array[j - 1]
        elif i < n and patt[j] != orgn_string[i]:
            if j != 0:
                j = prefix_array[j - 1]
            else:
                i += 1

    return location if location > 0 else -1



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

def main():
    # Leer el contenido de los archivos .txt y almacenarlos como cadenas
    mcode1 = read_file("mcode1.txt")
    mcode2 = read_file("mcode2.txt")
    mcode3 = read_file("mcode3.txt")
    trasmission1 = read_file("transmission1.txt")
    trasmission2 = read_file("transmission2.txt")



    # array to store the locations of the pattern
    location_array = [0] * len(trasmission1)

    # Buscar la cadena mcode1 en las transmisiones
    index1 = pattern_search(trasmission1, mcode1, location_array)
    if index1 == -1:
        print("False")
    for i in range(index1):
            print("True:", location_array[i])
    location_array = [0] * len(trasmission1)

    index1 = pattern_search(trasmission2, mcode1, location_array)
    if index1 == -1:
        print("False")
    for i in range(index1):
            print("True:", location_array[i])

    # Ejemplo de uso
    s = trasmission1
    P = manacher(s)
    print("El palindromo mas grande es de longitud:", max(P))

    # Opcional: Mostrar los palíndromos basados en P
    palindromos = []
    for i in range(1, len(P) - 1):
        longitud = P[i]
        if longitud > 0:
            start = (i - longitud) // 2
            palindromos.append(s[start:start + longitud])

    palindromoMasLargo1 = max(palindromos, key=len)
    print("Palíndromos encontrados:", palindromoMasLargo1)
    

    location_array = [0] * len(trasmission1)
        # Buscar la cadena mcode1 en las transmisiones
    index1 = pattern_search(trasmission1, palindromoMasLargo1, location_array)
    if index1 == -1:
        print("False")
    for i in range(index1):
            print("True:", location_array[i])
    location_array = [0] * len(trasmission1)


    


if __name__ == "__main__":
    main()
