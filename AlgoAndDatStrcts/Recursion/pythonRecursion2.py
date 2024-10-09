def flatten(arr,s):
    for i in arr:
        if isinstance(i, list):
            flatten(i,s)
        else:
            s.append(i)
    return s
            
def flatten2(arr):
    result = []  # Crear una nueva lista para almacenar los elementos planos
    for i in arr:
        if isinstance(i, list):
            result.extend(flatten2(i))  # Extender la lista con los elementos planos de la sublista
        else:
            result.append(i)  # Agregar el elemento si no es una lista
    return result




s = []

print(flatten2([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]])) # [1, 2, 3, 4, 5]


def capitalizeFirst(arr):
    if len(arr) == 0:
        return []
    else:
        a = arr[0]
        a = a.capitalize()
        return  [a] + capitalizeFirst(arr[1:])

print(capitalizeFirst(['car', 'taco', 'banana']))
