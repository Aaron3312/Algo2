def remove_duplicates(lst):
    unique_lst = [lst[0]]
    for item in lst[1:]:
        if item not in unique_lst:
                unique_lst.append(item)
    return unique_lst
 
my_list = [1, 1, 2, 2, 3, 4, 5]
print(remove_duplicates(my_list))  # Output: [1, 2, 3, 4, 5]