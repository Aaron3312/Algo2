# Max Product of Two Integers
# Find the maximum product of two integers in an array where all elements are positive.

# Example

# arr = [1, 7, 3, 4, 9, 5] 
# max_product(arr) # Output: 63 (9*7)

def max_product(arr):
    # TODO
    maxNum1 = arr[0]
    maxNum2 = arr[0]
    numbersMaximal = []

    for i in range (len(arr)):
        if maxNum1 < arr[i]:
            maxNum1 = arr[i]
            numbersMaximal.append(i)
            # print(maxNum1)
    print("sordooo", numbersMaximal)
    numbersMaximal.pop()
    maxNum2 = arr[numbersMaximal.pop()]
    print(maxNum2)
    print(maxNum1)
    return(maxNum2 * maxNum1)
            





arr = [1, 7, 3, 4, 9, 5,23,32,1,23,4,65,8,90,5,6,73,4,5,6,7,2] 
print(max_product(arr))