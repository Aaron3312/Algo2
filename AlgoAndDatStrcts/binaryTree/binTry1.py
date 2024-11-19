class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    
    def __str__(self):
        if self.data:
            data1 = str(self.data)
            return data1
    



def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else: 
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "node Succesfully inserted"

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

        
        
newBST = BSTNode(12)
print(insertNode(newBST, 11 ))
print(insertNode(newBST, 10 ))
print(insertNode(newBST, 9 ))
print(insertNode(newBST, 8 ))
print(insertNode(newBST, 7 ))
print(insertNode(newBST, 22 ))
print(insertNode(newBST, 33 ))
print(insertNode(newBST, 12 ))
print(insertNode(newBST, 23 ))



preOrderTraversal(newBST)
