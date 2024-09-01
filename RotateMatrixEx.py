# Rotate Matrix/ Image - LeetCode 48
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.

# DO NOT allocate another 2D matrix and do the rotation.

# Example:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# input: matrix 2x2 = 


def rotate(matrix):
    n = len(matrix)
 
    # Transpose the matrix
    for i in range(n):  # Iterate over the rows
        for j in range(i, n):  # Iterate over the columns starting from the current row 'i'
            # Swap the elements at positions (i, j) and (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
 
    # Reverse each row
    for row in matrix:  # Iterate over each row in the matrix
        row.reverse()  # Reverse the elements in the current row
        
        

 
    print(len(matrix))
    return matrix
    




matrix4 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

matrix = [[1,2,3],[4,5,6],[7,8,9]]
m2 = [[1,2],[3,4]]

print(rotate(matrix))
print(rotate(m2))
print(rotate(matrix4))