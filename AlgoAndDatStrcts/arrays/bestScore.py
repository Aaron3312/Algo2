# Best Score
# Given a list, write a function to get first, second best scores from the list.

# List may contain duplicates.

# Example

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]


def first_second(my_list):
    max1 = 0
    max2 = 0
    listD = []


    for i in range(len(my_list)):
        if max1 < my_list[i]:
            max1 = my_list[i]
            listD.append(i)
            print(listD)
    listD.pop()
    max2 = my_list[listD.pop()]
    return (max1, max2)




print(first_second(myList)) # 90 87