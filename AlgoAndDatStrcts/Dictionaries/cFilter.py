# Conditional Filter
# Define a function that takes a dictionary as a parameter and returns a dictionary with elements based on a condition.

# Example:

# Output:

# {'b': 2, 'd': 4}


def filter_dict(my_dict, condition):
    return {k: v for k, v in my_dict.items() if condition(k, v)}



my_dict12 = {'a': 1, 'b': 2, 'c': 3, 'd': 4} 
filtered_dict = filter_dict(my_dict12, lambda k, v: v % 2 == 0) 
print(filtered_dict)


# Same Frequency
# Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.

# Example:

# Output:

# False

def check_same_frequency(list1, list2):
    list1.sort()
    list2.sort()
    for i in range(len(list1)):
        if list1[i]!=list2[i]:
            return False
    return True



def check_same_frequency2(list1, list2):
    def count_elements(lst):
        counter = {}
        for element in lst:
            counter[element] = counter.get(element, 0) + 1
        return counter
    
    return count_elements(list1) == count_elements(list2)

list1 = [1, 2, 3, 2, 2]
list2 = [3, 1, 2, 1, 3]
print(check_same_frequency(list1, list2))
print(check_same_frequency2(list1, list2))

