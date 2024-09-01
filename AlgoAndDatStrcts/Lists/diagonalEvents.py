myList2D= [[1,2,3],[4,5,6],[7,8,9]] 

def diagonal_sum(matrix):
    dlista=[]
    for i in range(len(matrix)):
        dlista.append(matrix[i][i])
    return(sum(dlista))
        


print(len(myList2D))
print(diagonal_sum(myList2D))