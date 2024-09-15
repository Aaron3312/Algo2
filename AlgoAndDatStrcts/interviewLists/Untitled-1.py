def min_deletions_to_anagram(dna):
    anagram_list = []

    # Iterar sobre cada par de strings en cada lista de DNA
    for comparison in dna:
        for pair in comparison:
            count1 = {}
            count2 = {}

            # Contar letras en el primer string
            for char in pair[0]:
                if char in count1:
                    count1[char] += 1
                else:
                    count1[char] = 1
            
            # Contar letras en el segundo string
            for char in pair[1]:
                if char in count2:
                    count2[char] += 1
                else:
                    count2[char] = 1

            deletions = 0

            # Comparar los diccionarios de conteo y sumar diferencias
            for char in count1:
                if char in count2:
                    deletions += abs(count1[char] - count2[char])
                else:
                    deletions += count1[char]
            
            for char in count2:
                if char not in count1:
                    deletions += count2[char]

            if deletions == 0:
                anagram_list.append(1)
            else:
                anagram_list.append(0)
    
    return anagram_list

# Ejemplo de uso
dna = [
    [["abc", "cba"], ["xyz", "yzx"]],  # Primera lista de comparaciones
    [["hello", "bello"], ["abc", "def"]]  # Segunda lista de comparaciones
]

print(min_deletions_to_anagram(dna))  # Procesa múltiples comparaciones

