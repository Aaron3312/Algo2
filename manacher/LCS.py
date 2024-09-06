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
    longest_sequence = str1[max_position:max_position + max_length]

    return longest_sequence, max_position

str1 = open("ActIntegradora/transmission1.txt", "r").read()
str2 = open("ActIntegradora/transmission2.txt", "r").read()

sequence, position = find_longest_common_sequence(str1, str2)
print("Secuencia común más larga:", sequence)
print("Posición de inicio en la primera cadena:", position)