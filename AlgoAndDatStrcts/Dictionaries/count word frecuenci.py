# Count Word Frequency
# Define a function to count the frequency of words in a given list of words.

# Example:

# count_word_frequency(words) 
# Output:

#  {'apple': 3, 'orange': 2, 'banana': 1}


def count_word_frequency(words):
    frequency = {word: words.count(word) for word in words}
    return frequency



words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
print(count_word_frequency(words))


# Common Keys
# Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.

# Example:

# Output:

# {'a': 1, 'b': 5, 'c': 7, 'd': 5}


def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return 'The value does not exist'
# print(searchDict(myDict, 27))

def merge_dicts(dict1, dict2):
    mergerDictor = {key: (dict1[key] + dict2.get(key, 0)) for key in dict1}
    for key in dict2:
        if key not in (dict1):
            mergerDictor[key] = dict2[key]
    return(mergerDictor)

def merge_dicts1(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        result[key]= result.get(key, 0) + value
    return result


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print(merge_dicts(dict1, dict2))
print(merge_dicts1(dict1, dict2))




# Key with the Highest Value
# Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.

# Example:

# max_value_key(my_dict))
# Output:

# b




def max_value_key(my_dict):
    hkey = -10000
    keybig = ""
    for key, value in my_dict.items():
        if value > hkey :
            keybig = key
            hkey = value
    return keybig

def max_value_key1(my_dict):
    return max(my_dict, key=my_dict.get)

my_dict = {'a': 5, 'b': 9, 'c': 2}

print(max_value_key(my_dict))
print(max_value_key1(my_dict))

# Reverse Key-Value Pairs
# Define a function which takes as a parameter dictionary and returns a dictionary in which everse the key-value pairs are reversed.

# Example:

# Output:

# {1: 'a', 2: 'b', 3: 'c'}


def reverse_dict(my_dict1):
    dict1 = {}
    for key, value in my_dict1.items():
        dict1[value] =key

    return dict1

def reverse_dict1(my_dict):
    return {v: k for k, v in my_dict.items()}



my_dict1 = {'a': 1, 'b': 2, 'c': 3}
print(reverse_dict(my_dict1))


# Conditional Filter
# Define a function that takes a dictionary as a parameter and returns a dictionary with elements based on a condition.

# Example:

# Output:

# {'b': 2, 'd': 4}


def filter_dict(my_dict, condition):
    return {k: v for k, v in my_dict.items() if condition(k, v)}



my_dict12 = {'a': 1, 'b': 2, 'c': 3, 'd': 4} 
filtered_dict = filter_dict(my_dict12, lambda k, v: v % 2 == 0) 



