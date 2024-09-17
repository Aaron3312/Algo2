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
    if n < 1:
        return 1
    else:
        return n* factorial(n-1)
    
print(factorial(10))