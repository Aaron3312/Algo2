def read_file_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            
            # Listas para almacenar los números
            numeros_izquierda = []
            numeros_derecha = []
            
            # Procesar cada línea
            for line in lines:
                # Dividir la línea en dos números usando split()
                nums = line.strip().split()
                
                # Verificar que la línea tenga dos números
                if len(nums) == 2:
                    numeros_izquierda.append(int(nums[0]))
                    numeros_derecha.append(int(nums[1]))
            
            return numeros_izquierda, numeros_derecha
            
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{filename}'")
        return [], []
    except Exception as e:
        print(f"Error al leer el archivo: {str(e)}")
        return [], []
    
def find_minNumAndPop(list):
    minNum = min(list)
    list.remove(minNum)
    return minNum

def findDistanceBetween(num1, num2):
    return abs(num1 - num2)

def workListOut(izq, der):
    total = 0
    for i in range(len(izq)):
        total += findDistanceBetween(find_minNumAndPop(izq), find_minNumAndPop(der))
    return total

def howManyThimesAppearLeftinRight(izq, der):
    numbersDict = {}
    total = 0
    for i in range(len(izq)):
        while izq[i] in der:
            if izq[i] in der:
                numbersDict[izq[i]] = numbersDict.get(izq[i], 0) + 1
                der.remove(izq[i])
        
    for i in numbersDict:
        print(f"{i} aparece {numbersDict[i]} veces en la lista derecha ")
        total += i * numbersDict[i]
    return total



izq, der = read_file_lines("1.txt")
print(howManyThimesAppearLeftinRight(izq, der))