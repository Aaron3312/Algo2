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

input_tuple = ('Hello', 'World', 'from', 'Python')
output_string = concatenate_strings(input_tuple)
print(output_string)  # Expected output: 'Hello World from Python'
