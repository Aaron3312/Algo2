import numpy as np

myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])


def numberFinder(array, num):
    for i in range(len(array)):
        if array[i] == num:
            print(i)


numberFinder(myArray, 4)