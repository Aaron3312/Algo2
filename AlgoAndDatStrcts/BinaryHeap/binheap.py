

class Heap:
    def __init__(self, size):
        self.customList = (size+1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1

def peekofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customList[1]
    
def sizeOfHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize

def levelOrderTrav(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1, rootNode.heapSize+1):
            print(rootNode.customList[i])

def insertNode(rootNode, index, heapType):
    parentIndex = int(index/2)
    if index <= 1:
        print("the value has 1")
        return
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        insertNode(rootNode, parentIndex, heapType)
    elif heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        insertNode(rootNode, parentIndex, heapType)

def instertNodeOf(rootNode, nodeValue, heapType):
    if rootNode.heapSize +1 == rootNode.maxSize:
        return "the binary heap is full"
    rootNode.customList[rootNode.heapSize +1] = nodeValue
    rootNode.heapSize += 1
    insertNode(rootNode, rootNode.heapSize, heapType)

def heapifyTreeExtract(rootNode, index, heapType):
    parentIndex = index
    leftIndex = 2 * index
    rightIndex = 2 * index + 1
    
    # Verificar si hay hijo izquierdo y si debemos intercambiar con él
    if leftIndex <= rootNode.heapSize:
        if heapType == "Max":
            if rootNode.customList[leftIndex] > rootNode.customList[parentIndex]:
                parentIndex = leftIndex
        else:
            if rootNode.customList[leftIndex] < rootNode.customList[parentIndex]:
                parentIndex = leftIndex
    
    # Verificar si hay hijo derecho y si debemos intercambiar con él
    if rightIndex <= rootNode.heapSize:
        if heapType == "Max":
            if rootNode.customList[rightIndex] > rootNode.customList[parentIndex]:
                parentIndex = rightIndex
        else:
            if rootNode.customList[rightIndex] < rootNode.customList[parentIndex]:
                parentIndex = rightIndex
    
    # Si el índice del padre cambió, hacer el intercambio y seguir heapifying
    if parentIndex != index:
        temp = rootNode.customList[index]
        rootNode.customList[index] = rootNode.customList[parentIndex]
        rootNode.customList[parentIndex] = temp
        heapifyTreeExtract(rootNode, parentIndex, heapType)

def extractNode(rootNode, heapType):
    if rootNode.heapSize == 0:
        return None
    
    # Guardar el valor a extraer
    extractedNode = rootNode.customList[1]
    
    # Mover el último elemento a la raíz
    rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
    rootNode.customList[rootNode.heapSize] = None
    rootNode.heapSize -= 1
    
    # Reordenar el heap solo si quedan elementos
    if rootNode.heapSize > 0:
        heapifyTreeExtract(rootNode, 1, heapType)
    
    return extractedNode

    


newBinaryHeap = Heap(5)
print(sizeOfHeap(newBinaryHeap))


instertNodeOf(newBinaryHeap, 4,"Max")
instertNodeOf(newBinaryHeap, 5,"Max")
instertNodeOf(newBinaryHeap, 2,"Max")
instertNodeOf(newBinaryHeap, 1,"Max")

print(extractNode(newBinaryHeap, "Max"))

print("sht")
levelOrderTrav(newBinaryHeap)

