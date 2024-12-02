def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list [pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, swap_index, pivot_index)
    return swap_index

def quickSort(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quickSort(my_list, left, pivot_index-1)
        quickSort(my_list, pivot_index+1, right)
    return my_list
def heapify(customList, n, i):
    smallest = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and customList[l] < customList[smallest]:
        smallest = l

    if r < n and customList[r] < customList[smallest]:
        smallest = r
    
    if smallest != i:
        customList[i], customList[smallest] = customList[smallest], customList[i]
        heapify(customList,n,smallest)

def heapSort(customList):
    n = len(customList)
    for i in (range(int(n/2)-1,-1,-1)):
        heapify(customList, n, i)
    
    for i in range(n-1,0,-1):
        customList[i], customList[0] = customList[0], customList[i]
        heapify(customList, i, 0)
    customList.reverse()

my_list = [-33,3,5,0,6,2,1,4,-2]

# print(pivot(my_list, 0, 6))

# print(quickSort(my_list,0,6))
print(my_list)
heapSort(my_list)
print(my_list)


