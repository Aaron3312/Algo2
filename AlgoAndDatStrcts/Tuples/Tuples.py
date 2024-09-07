tuples = ("a","b", "c", "d", "e")

print("a" in tuples)


tuples.index("a")

print(min(tuples))


init_tuple = [(0, 1), (1, 2), (2, 3)]
 
result = sum(n for _, n in init_tuple)
 
print(result)




# Sum and Product
# Write a function that calculates the sum and product of all elements in a tuple of numbers.

# Example

def sum_product(input_tuple):
    counter = 0
    product = 1
    for i in range(len(input_tuple)):
        counter = input_tuple[i] + counter
        product = product * input_tuple[i]

    return counter, product
        

input_tuple = (1, 2, 3, 4)

sum_result, product_result = sum_product(input_tuple)

#
print(sum_result, product_result)  # Expected output: 10, 24




# Elementwise Sum
# Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.

# Example


def tuple_elementwise_sum(tuple1, tuple2):
    tuple3 = ()
    for i in range(len(tuple1)):
        tuple3 = tuple3 + (tuple1[i] + tuple2[i],)
    return tuple3

    
    


tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
output_tuple = tuple_elementwise_sum(tuple1, tuple2)
print(output_tuple)  # Expected output: (5, 7, 9)




# Insert at the Beginning
# Write a function that takes a tuple and a value, and returns a new tuple with the value inserted at the beginning of the original tuple.

# Example




def insert_value_front(input_tuple, value_to_insert):
    deadlifter = (value_to_insert,)
    deadlifter = deadlifter + input_tuple
    return deadlifter



input_tuple = (2, 3, 4)
value_to_insert = 1
output_tuple = insert_value_front(input_tuple, value_to_insert)
print(output_tuple)  # Expected output: (1, 2, 3, 4)



# Concatenate
# Write a function that takes a tuple of strings and concatenates them, separating each string with a space.

# Example

def concatenate_strings(input_tuple):
    textual = ""
    for i in range(len(input_tuple)):
        if i == len(input_tuple) - 1:
            textual = textual + input_tuple[i]
        else:
            textual = textual + input_tuple[i] + " "
    return(textual)


input_tuple23 = ('Hello', 'World', 'from', 'Python')
output_string = concatenate_strings(input_tuple23)
print(output_string)  # Expected output: 'Hello World from Python'




# Diagonal
# Create a function that takes a tuple of tuples and returns a tuple containing the diagonal elements of the input.

# Example


def get_diagonal(tup):
    deadlof = ()
    for i in range(len(tup)):
        deadlof = deadlof + (tup[i][i],)
    return deadlof


input_tuple123 = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
output_tuple = get_diagonal(input_tuple123)
print(output_tuple)  # Expected output: (1, 5, 9)




# Common Elements
# Write a function that takes two tuples and returns a tuple containing the common elements of the input tuples.

# Example



print("Common elements")
def common_elements(tuple1, tuple2):
    deadlif23 = ()
    for i in range(len(tuple1)):
        for j in range( len(tuple2)):
            if tuple1[i] == tuple2[j]:
                deadlif23 = deadlif23 + (tuple1[i],)
    return(deadlif23)

def common_elements1(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))

tuple133 = (1, 2, 3, 4, 5)
tuple233 = (4, 5, 6, 7, 8)
output_tuple1 = common_elements(tuple133, tuple233)
print(output_tuple1)  # Expected output: (4, 5)
