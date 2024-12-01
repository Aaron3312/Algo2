class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.value = None


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.numbers = {
            "one": "1", "two": "2", "three": "3", "four": "4",
            "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
        }
        for word, value in self.numbers.items():
            self.insert(word, value)

    def insert(self, word, value):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.value = value

    def insertString(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch:node})
                
            current = node
        current.endOfString = True

    def searchString(self,word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node == None:
                return False
            currentNode = node

        if currentNode.endOfString == True:
            return True
        else:
            return False
        

    def find_number(self, text, start_pos=0):
 
        node = self.root
        for i in range(start_pos, len(text)):
            if text[i] in node.children:
                node = node.children[text[i]]
                if node.is_end:
                    return i, node.value
            else:
                return None, None
        return None, None
    

# Abrimos el archivo y leemos las líneas en una lista
def read_file_lines(filename):
    try:
        with open(filename, 'r') as file:
            # readlines() lee todas las líneas y las guarda en una lista
            lines = file.readlines()
            
            # Eliminamos los caracteres de nueva línea y espacios en blanco
            lines = [line.strip() for line in lines]
            
            return lines
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{filename}'")
        return []
    except Exception as e:
        print(f"Error al leer el archivo: {str(e)}")
        return []



def first(line):
    trie = Trie()
    min_pos = float("inf")
    first_digit = None
    for i, char in enumerate(line):
        if char.isdigit():  # Solo para strings positivos
            min_pos = i
            first_digit = char
            break

    for i in range(len(line)):
        pos, value =trie.find_number(line,i)
        if pos is not None and i < min_pos:
            min_pos = i
            first_digit = value
    
    return first_digit

def last(line):
    trie = Trie()
    max_pos = -1
    last_digit = None
    
    # Buscar último dígito numérico
    for i, char in enumerate(line):
        if char.isdigit():
            max_pos = i
            last_digit = char
    
    # Buscar último número escrito en letras
    for i in range(len(line)):
        pos, value = trie.find_number(line, i)
        if pos is not None and pos > max_pos:
            max_pos = pos
            last_digit = value
            
    return last_digit



def readFirstAndLast(lines1):
    count = 0
    for line in lines1:
        count1 = first(line)
        count2 = last(line)
        count3 = count1 + count2
        count += int(count3)
    return count



validNums =[ "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]

# Ejemplo de uso
filename = "1.txt"
lines = read_file_lines(filename)
lines1 = lines[:2]
print(readFirstAndLast(lines))


# Verificamos si se obtuvieron líneas
# if lines:
#     print("Líneas leídas:")
#     for i, line in enumerate(lines, 1):
#         print(f"Línea {i}: {line}")
