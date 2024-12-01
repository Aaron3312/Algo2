

import math
 
def countZeroes(customList):
    left = 0
    right = len(customList)-1
    while left <= right:
        middle = math.floor((left + right)/2)
        print (middle)
        if customList[middle] == 1:
            left = middle + 1
        else:
            right = middle - 1
    return len(customList) - left




# print(countZeroes([1,1,1,1,0,0]))  # 2
# print(countZeroes([1,0,0,0,0]))  # 4
# print(countZeroes([0,0,0]))  # 3
# print(countZeroes([1,1,1,1]))  # 0

# # Test Case 1: Transition point exactly at middle
# print(countZeroes([1,1,1,0,0,0]))  # Expected: 3, But might get wrong result
# # This can fail because the half calculation with round() might not hit the exact transition

# # # Test Case 2: Array with odd length and transition near middle
# print(countZeroes([1,1,1,1,0,0,0]))  # Can get stuck in recursion or give wrong result

# # # Test Case 3: Transition point near end
# print(countZeroes([1,1,1,1,1,0]))  # Will likely fail due to wrong half calculation

# # # Test Case 4: Longer array with transition point after middle
# print(countZeroes([1,1,1,1,1,1,1,1,0,0]))  # Will fail due to recursive case not handling this pattern

# # # Test Case 5: Array of length 2
print(countZeroes([1,0]))  # Can fail due to half calculation being 0

# # Test Case 6: Very long array with transition near end
# zeros = [0] * 50
# ones = [1] * 950
# test_array = ones + zeros
# print(countZeroes(test_array))  
# # Will likely give wrong result due to recursive case not properly handling large arrays