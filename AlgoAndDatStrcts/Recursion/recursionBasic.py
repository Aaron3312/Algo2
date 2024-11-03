def productOfArray(arr):
    if arr:
        return (arr.pop() * productOfArray(arr))
    else:
        return (1)
    



print(productOfArray([1,2,3])) # 6
print(productOfArray([1,2,3,10])) # 60
print(productOfArray([10,2,3,10])) # 300