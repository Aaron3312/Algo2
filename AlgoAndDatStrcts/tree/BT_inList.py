class BinaryTree:
    def __init__(self,size):
        self.customList = size * [None]
        self.lastUseIndex = 0
        self.maxSize = size
    
    def insertNode(self,value):
        if self.lastUseIndex + 1 >= self.maxSize:  # Adjusted boundary condition
            return "the BinaryTree is full"
        self.customList[self.lastUseIndex+1] = value
        self.lastUseIndex +=1
        return "the value has been sucessfully inserted"
    
    def searchNode(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Success"
        return "Not Found"
    
    def PreOrderTraversal(self, index):
        if index > self.lastUseIndex:
            return
        print(self.customList[index])
        self.PreOrderTraversal(index*2)
        self.PreOrderTraversal(index*2+1)

    def inOrderTraversal(self, index):
        if index > self.lastUseIndex:
            return
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal(index*2+1)

    def posOrderTraversal(self, index):
        if index > self.lastUseIndex:
            return
        self.posOrderTraversal(index*2)
        self.posOrderTraversal(index*2+1)
        print(self.customList[index])
    
    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUseIndex+1):
            print(self.customList[i])

    def deleteNode(self, value):
        if self.lastUseIndex == 0:
            return "There is not any node to delete"
        for i in range (1, self.lastUseIndex+1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUseIndex]
                self.customList[self.lastUseIndex] = None
                self.lastUseIndex -= 1
                return "the node have been sucessfully deleted"
            
    def deleteList(self):
        self.customList = None

newBT = BinaryTree(8)

print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
print(newBT.insertNode("Tea"))
print(newBT.insertNode("Coffe"))

print(newBT.searchNode("Cold"))

newBT.deleteNode("Hot")

newBT.levelOrderTraversal(1)




