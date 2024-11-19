class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    
    def __str__(self):
        if self.data:
            data1 = str(self.data)
            return data1
    

def minValueNode(bstNode):
    current = bstNode
    while current.leftChild is not None:
        current = current.leftChild
    return current
    
def maxValueNode(bstNode):
    current = bstNode
    while current.rightChild is not None:
        current = current.rightChild
    return current

def deletedNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftChild = deletedNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deletedNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp

        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deletedNode(rootNode.rightChild, temp.data)
    return rootNode    



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
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def levelOrderTrav(rootNode):
    if not rootNode:
        return
    else:
        queue = []
        queue.append(rootNode)
        while queue != []:
            root = queue.pop(0)
            print(root.data)
            if root.leftChild is not None:
                queue.append(root.leftChild)
            if root.rightChild is not None:
                queue.append(root.rightChild)

def Find(rootNode, data):
    if rootNode.data == data:
        print("valueFund")
        return
    elif rootNode.data > data:
        if rootNode.leftChild:
            Find(rootNode.leftChild, data)
        else:
            print ("notFound")
    elif rootNode.data <= data:
        if rootNode.rightChild:
            Find(rootNode.rightChild, data)
        else:
            print ("notFound")

    else:
        print ("notFound")
        return

def deleteTree(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None

    return "deleted"


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

Find(newBST, 32)

(deletedNode(newBST,12))


deleteTree(newBST)


levelOrderTrav(newBST)
