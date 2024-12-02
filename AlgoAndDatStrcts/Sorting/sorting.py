import math
import random

def bubbleSort(customList):
    for i in range(len(customList)-1):
        for j in range(len(customList)-i-1):
            if customList[j] > customList[j + 1]:
                customList[j], customList[j+1] = customList[j+1], customList[j]
    print(customList)

def selectionSort(customList):
    for i in range(len(customList)):       # i recorre desde 0 hasta len(customList)-1
        min_index = i                      # Asumimos que el primer elemento es el mínimo
        for j in range(i+1, len(customList)):    # j recorre desde i+1 hasta el final
            if customList[min_index] > customList[j]:  # Si encontramos un número menor
                min_index = j              # Actualizamos el índice del mínimo
        # Intercambiamos los elementos
        print(customList)
        customList[i], customList[min_index] = customList[min_index], customList[i]

# Insertion Sort
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Elemento a insertar
        j = i - 1     # Índice para recorrer la parte ordenada
        # Mueve elementos mayores que key una posición adelante
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Inserta key en su posición correcta
    return arr


def bucketSort(customList):
    # 1. Determinar número de cubos
    numberofBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    
    # 2. Crear cubos vacíos
    arr = [[] for _ in range(numberofBuckets)]
    
    # 3. Distribuir elementos en cubos
    for num in customList:
        # Fórmula para determinar a qué cubo va cada elemento
        index_b = math.ceil(num * numberofBuckets / maxValue)
        arr[index_b - 1].append(num)
    
    # 4. Ordenar cada cubo usando insertion sort
    for i in range(numberofBuckets):
        arr[i] = insertionSort(arr[i])
    
    # 5. Concatenar todos los cubos en la lista final
    k = 0
    for i in range(numberofBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return customList

def is_sorted(arr):
    """Verifica si la lista está ordenada"""
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

def bogo_sort(arr):
    """
    Bogo Sort: Revuelve la lista aleatoriamente hasta que quede ordenada
    """
    attempts = 0
    while not is_sorted(arr):
        random.shuffle(arr)
        attempts += 1
        if attempts % 100000 == 0:  # Para evitar bucles infinitos en la práctica
            print(f"Intento {attempts}, lista actual: {arr}")
    return arr, attempts

cList = [2,1,7,6,5,3,4,9,8]

# bubbleSort(cList)
# selectionSort(cList)
# insertionSort(cList)
print(bucketSort(cList))

# numbers = [2,1,7,6,5,3,4,9,8,2,1,7,6,5,3,4,9,8]
# print("Lista original:", numbers)
# sorted_numbers, total_attempts = bogo_sort(numbers.copy())
# print("Lista ordenada:", sorted_numbers)
# print("Número total de intentos:", total_attempts)