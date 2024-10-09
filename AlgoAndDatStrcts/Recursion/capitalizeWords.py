words = ['i', 'am', 'learning', 'recursion']
# words = []

def capitalizeWords(arr):
    if arr == []:
        return []
    else:
        a = arr[0]
        a = a.upper()
        return [a] + capitalizeWords(arr[1:])
    

print(capitalizeWords(words))