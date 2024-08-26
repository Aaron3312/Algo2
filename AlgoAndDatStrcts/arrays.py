import array
import numpy as np

def findBiggestNumber(array):
    biggest = array[0]
    for i in range(len(array)):
        if array[i] > biggest:
            biggest = array[i]
    return biggest

arrays = [1 , 32, 345, 54, 32, 43,54 ,65,54,343]
print(findBiggestNumber(arrays))



deadArray = np.array([], dtype=int)

ar = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(ar)
ar.insert(0, 100)
print(ar)

asdas = array.array('i', [5, 2, 3, 4, 5, 6, 7, 8, 5, 10])
print(asdas)

def linear_search(array, item):
    for i in range(len(array)):
        if array[i] == item:
            return i
    return None

print(linear_search(asdas, 5))

