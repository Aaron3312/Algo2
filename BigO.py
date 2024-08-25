def multiply_numbers(n):
    return n * n

def print_items(n):
    for item in range(n):
        for item2 in range(n):
            for item3 in range(n):
                for item4 in range(n):
                    for item5 in range(n):
                        for item6 in range(n):
                            for item7 in range(n):
                                for item8 in range(n):
                                    print(item, item2, item3, item4, item5, item6, item7, item8)
print_items(1)

def sum(n):
    if n <= 0:
        return 0
    return n + sum(n-1)

print(sum(10))



def findBiggestNumber(array):
    biggest = array[0]
    for i in range(len(array)):
        if array[i] > biggest:
            biggest = array[i]
    return biggest

array = [1 , 32, 345, 54, 32, 43,54 ,65,54,343]
print(findBiggestNumber(array))