def linearSearch(array, val):
    for i in range(len(array)-1):
        if array[i] == val:
            print("yes Bitch")
            break

def binarySearch(array, val):
    len1 = len(array)
    middle = round(len1/2)
    print("funcion llamada")
    if val == array[middle]:
        print("si bro")
        return
    if len1 <= 1:
        print("no hay bro")
        return
    elif val > array[middle]:
        binarySearch(array[middle:], val)
    elif val < array[middle]:
        binarySearch(array[:middle], val)
    

def generate_large_sorted_list(size=7, start=0, step=2):
    """
    Genera una lista ordenada de números
    size: tamaño de la lista
    start: número inicial
    step: incremento entre números
    """
    large_list = list(range(start, start + size * step, step))
    return large_list

# Generar la lista
numeros = generate_large_sorted_list() 

m2 = [1,4,3,2,5,6,78,56,33,2,22]
m3 = [-2500, -1337, -999, -750, -500, -333, -222, -111, -50, -25, -10, -5, -1,
                     0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 100, 150, 200, 250, 
                     333, 444, 555, 666, 777, 888, 999, 1111, 2222, 3333, 
                     4444, 5555, 6666, 7777, 8888, 9999, 10000, 12345, 
                     15000, 20000, 25000, 50000, 75000, 99999]
# linearSearch(m2, 2)
binarySearch(numeros, 12)