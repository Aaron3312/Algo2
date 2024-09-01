def missing_number(arr, n):
    # TODO
    counter = 0
    for i in arr:
        if ( 0 > (counter-1)):
            ant = 0
        else:
            ant = arr[counter - 1]
        print(ant)
        if ((ant+1) != arr[counter]):
            return (ant+1)
        counter = counter + 1



arr = [1,2,3,4,6]
n = 6

print(missing_number(arr,n))
