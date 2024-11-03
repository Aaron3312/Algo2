def build_suffix_array(s):
    # Crear una lista de sufijos y sus índices originales
    suffixes = [(s[i:], i) for i in range(len(s))]
    # Ordenar los sufijos lexicográficamente
    suffixes.sort()
    # Retornar sólo los índices
    suffix_array = [suffix[1] for suffix in suffixes]
    sorted_suffixes = [suffix[0] for suffix in suffixes]  # Extraer los sufijos ordenados
    return suffix_array, sorted_suffixes

def binary_search_substring(s, suffix_array, substring):
    left, right = 0, len(suffix_array) - 1
    while left <= right:
        mid = (left + right) // 2
        suffix_start = suffix_array[mid]
        suffix = s[suffix_start:suffix_start + len(substring)]
        
        if suffix == substring:
            return suffix_start  # Encontramos la posición del sufijo
        elif suffix < substring:
            left = mid + 1  # Buscar en la mitad derecha
        else:
            right = mid - 1  # Buscar en la mitad izquierda
    
    return -1  # No encontrado

# Cadena y substring a buscar
s = "alice in chains"
substring = "ice"

# Construir el suffix array y obtener los sufijos ordenados
suffix_array, sorted_suffixes = build_suffix_array(s)

# Imprimir el array de sufijos ordenados y el suffix array
print(f'Sufijos ordenados lexicográficamente: {sorted_suffixes}')
print(f'Suffix Array = {suffix_array}')

# Buscar la substring usando búsqueda binaria
position = binary_search_substring(s, suffix_array, substring)

# Resultado
if position != -1:
    print(f'La substring "{substring}" se encuentra en la posición {position}.')
else:
    print(f'La substring "{substring}" no se encuentra en la cadena.')
