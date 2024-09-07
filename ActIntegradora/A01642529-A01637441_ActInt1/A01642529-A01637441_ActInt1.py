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

def find_longest_common_sequence(str1, str2):
    m = len(str1)
    n = len(str2)

    # Crear una lista de listas iniciadas en 0
    # para almacenar las longitudes de las subsecuencias
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Variables para almacenar la longitud y la posición de la secuencia común más larga
    max_length = 0
    max_position = 0

    # Calcular las longitudes de las subsecuencias comunes
    # ya se que es cuadratica Aaron no te enojes
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    max_position = i - max_length

    # Obtener la secuencia común más larga y su posición
    # con slicing desde max_position hasta max_position + max_length
    #pero no la uso igual
    # longest_sequence = str1[max_position:max_position + max_length]

    return max_position, max_length

def encontrar_palindromo_mas_largo(trasmission):
    s = trasmission
    P = manacher(s)
    palindromos = []
    for i in range(1, len(P) - 1):
        longitud = P[i]
        if longitud > 0:
            start = (i - longitud) // 2
            palindromos.append(s[start:start + longitud])
    palindromoMasLargo = max(palindromos, key=len)
    location_array = [0] * len(trasmission)
    index1 = pattern_search(trasmission, palindromoMasLargo, location_array)
    if index1 == -1:
        print("False")
    for i in range(index1):
        print(location_array[i], location_array[i] + len(palindromoMasLargo))

def main():
    # Leer el contenido de los archivos .txt y almacenarlos como cadenas
    mcode1 = read_file("mcode1.txt")
    mcode2 = read_file("mcode2.txt")
    mcode3 = read_file("mcode3.txt")
    trasmission1 = read_file("transmission1.txt")
    trasmission2 = read_file("transmission2.txt")
    trasmission3 = read_file("transmission3.txt")


    #PARTE 1
    print("Parte 1")
    # Lista de códigos y transmisiones
    mcodes = [mcode1, mcode2, mcode3]
    transmissions = [trasmission1, trasmission2]

    # Iterar sobre cada combinación de código y transmisión
    for transmission in transmissions:
        for mcode in mcodes:
            location_array = [0] * len(transmission)
            index = pattern_search(transmission, mcode, location_array)
            if index == -1:
                print("False")
            for i in range(index):
                print("True:", location_array[i])

    #PARTE 2
    print("Parte 2")
    # Palíndromo más largo en la transmisión 1
    encontrar_palindromo_mas_largo(trasmission1)

    # Palíndromo más largo en la transmisión 2
    encontrar_palindromo_mas_largo(trasmission2)

    #PARTE 3
    print("Parte 3")
    position, max_length = find_longest_common_sequence(trasmission1, trasmission2)
    print(position, position + max_length)

if __name__ == "__main__":
    main()