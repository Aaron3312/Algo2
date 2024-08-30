integrers = [1, 2, 3, 4, 5, 1, 1, 1]

print(integrers[:])

integrers.remove(1)
integrers.remove(1)

del integrers[0:2]

print(integrers[:])



a = [1, 2, 3, 4, 5]

b = [6, 7, 8, 9, 10]

c = a + b
a.pop()


print(c)
print(a)
print(b)
print(min(c))


myList = list()


while (False):
    inp = input('Enter a number: ')
    if inp == 'd':
        break
    value = float(inp)
    myList.append(value)
    average = (sum(myList) / (len(myList)))



spm = "spam spam spam"
delimiter   = " "
print(spm.split(delimiter))


prevList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13, 14, 15, 16, 17, 18, 19, 20 , 100]
new_list = list()

for i in prevList:
    if i % 2 == 0:
        print(i)
        new_list.append(i)

print(new_list)

lenguaje = "Python"
newLenguaje = [letter for letter in lenguaje]

# for i in range(len(lenguaje)):
#     newLenguaje.append(lenguaje[i])


print(newLenguaje)