from array import *
import numpy as np

# Create an array whit an data type of integer, note all types of data types are: b, B, u, h, H, i, I, l, L, q, Q, f, d
my_array = array('i', [1, 2, 3, 4, 5])

for i in my_array:
    print(i)

my_array.append(6)

print(my_array)

my_array.insert(3, 11)

print(my_array)

my_array.remove(11)

print(my_array)

my_array1 = array('i', [10, 11, 12, 13, 14])
myArray = [1, 2, 3, 4, 5]
my_array.extend(my_array1)

print(my_array)


array2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

array2d = np.insert(array2d, 3, [1, 4, 3], axis=1)

print(array2d)

print(array2d[0][1])

def traverseTda(array, numSearch):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == numSearch:
                print("Number found at: ", i, j)
            else:
                print("Number not found at: ", i, j)

traverseTda(array2d, 4)

newArray2d = np.delete(array2d, 3, axis=1)

print(newArray2d)
