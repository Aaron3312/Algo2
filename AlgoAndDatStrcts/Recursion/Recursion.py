def first():
    second()
    print("I'm first")

def second():
    third()
    print("I'm second")

def third():
    fourth()
    print("I'm third")

def fourth():
    fifth()
    print("I'm fourth")

def fifth():
    print("I'm fifth")

# Call the first function to start the chain
first()


def recursive(n):
    if n<1:
        print("n is less than 1")
    else:
        recursive(n-1)
        print(n)

recursive(4)



def factorial(n):
    assert n >= 0 and int(n) == n, "the number need to be integer and positive"
    if n < 1:
        return 1
    else:
        return n* factorial(n-1)
    
print(factorial(5))


def fibonacci(n):
    assert n >= 0 and int(n) == n, "the number need to be integer and positive"
    if n in [0,1]:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
    

print(fibonacci(6))

