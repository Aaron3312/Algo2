#you need to make whit an array of integers, and a target sum, return indices of all the two numbers such that they add up to the target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

#Example 1:

#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Output: Because nums[0] + nums[1] == 9, we return [0, 1].

#Example 2:

#Input: nums = [3,2,4], target = 6
#Output: [1,2]


def pairsSolver(nums, target):
    for i in range (len(nums)):

        for j in range (i+1,len(nums)):
            print(i,j)
            if (nums[i] + nums[j]) == target:
                print ("HELLO",i, j)
    
nums = [3,6,2,4,5,3,1]
pairsSolver(nums, 6)
