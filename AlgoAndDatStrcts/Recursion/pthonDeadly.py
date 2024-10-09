
def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num == 2:
        return 1
    elif num == 3:
        return 2
    else:
        return (fib(num-1)+ fib(num-2))
    
print (fib(2))

def reverse(strng):
    # Caso base: si la cadena es vacía o tiene un solo carácter, se retorna la cadena tal cual
    if len(strng) == 0:
        return strng
    else:
        # Llamada recursiva eliminando el primer carácter y añadiéndolo al final
        return reverse(strng[1:]) + strng[0]

sstrings = "deadly"
dead = "ded"
print(reverse(sstrings))




def isPalindrome(strng):
    a  = reverse(strng)
    if a == strng:
        return True
    else:
        return False
    

print(isPalindrome(dead))


def isOdd(num):
    if num%2==0:
        return False
    else:
        return True
        
def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    
    if cb(arr[0]):
        return True
    
    
    return(someRecursive(arr[1:], isOdd)
)
    


print(someRecursive([4,6,8,1], isOdd))


