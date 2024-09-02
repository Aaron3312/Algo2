# Pairs
# Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.

# Example

# pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
# Output : ['2+5', '4+3', '3+4', '-2+9']



def pair_sum(myList, sum):
    # TODO
    killer = []
    for i in range(len(myList)):
        for j in range(1+i, len(myList)):
            if ((myList[i] + myList[j]) == sum ):
                killer.append(""+str(myList[i])+"+"+str(myList[j]))
    return killer


print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))

