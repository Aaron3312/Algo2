class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None



newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
RigthChild = TreeNode("Cold")
tea = TreeNode("Tea")
coffe = TreeNode("Coffe")
newBT.leftChild = leftChild
newBT.rightChild = RigthChild
leftChild.leftChild = tea
leftChild.rightChild = coffe


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
    

# preOrderTraversal(newBT)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


# inOrderTraversal(newBT)


def PostOrderTraversal(rootNode):
    if not rootNode:
        return
    PostOrderTraversal(rootNode.leftChild)
    PostOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

# PostOrderTraversal(newBT)
queue = []

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = []
        customQueue.append(rootNode)
        while customQueue != []:
            root = customQueue.pop(0)
            print(root.data)
            if (root.leftChild is not None):
                customQueue.append(root.leftChild)
            
            if (root.rightChild is not None):
                customQueue.append(root.rightChild)

# levelOrderTraversal(newBT)   

def searchOrderTraversal(rootNode, nodeValue):
    if not rootNode:
        return False
    else:
        customQueue = []
        customQueue.append(rootNode)
        while customQueue != []:
            root = customQueue.pop(0)
            # print(root.data)
            if (root.data == nodeValue):
                return True
            if (root.leftChild is not None):
                customQueue.append(root.leftChild)
            
            if (root.rightChild is not None):
                customQueue.append(root.rightChild)

# print (searchOrderTraversal(newBT, "Teaa")  )   


def insertMethod(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = []
        customQueue.append(rootNode)
        while customQueue != []:
            root = customQueue.pop(0)
            if root.leftChild is not None:
                customQueue.append(root.leftChild)
            else:
                root.leftChild = newNode
                return "Sucess"
            if root.rightChild is not None:
                customQueue.append(root.rightChild)
            else:
                root.leftChild = newNode
                return "Sucess"


newNode = TreeNode("Cola")
# print(insertMethod(newBT, newNode))

# levelOrderTraversal(newBT)

# preOrderTraversal(newBT)


def getDepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = []
        customQueue.append(rootNode)
        while customQueue != []:
            root = customQueue.pop(0)
            if (root.leftChild is not None):
                customQueue.append(root.leftChild)
            
            if (root.rightChild is not None):
                customQueue.append(root.rightChild)
        deepestNode = root
        return deepestNode

# dep = getDepestNode(newBT)

# print(dep.data)

def deleteDepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        customQueue = []
        customQueue.append(rootNode)
        while customQueue != []:
            root = customQueue.pop(0)
            if root == dNode:
                root = None
                return
            else:
                if (root.leftChild is not None and root.leftChild != dNode):
                    customQueue.append(root.leftChild)
                    print(root.leftChild.data)
                else:
                    if root.leftChild:
                        print("somenting was deleted " + root.leftChild.data)
                    root.leftChild = None


                if (root.rightChild is not None and root.rightChild != dNode):
                    print(root.rightChild.data)
                    customQueue.append(root.rightChild)
                else:
                    if root.rightChild:
                        print("somenting was deleted " + root.rightChild.data)
                    root.rightChild = None

# deleteDepestNode(newBT, dep)

# dep = getDepestNode(newBT)

# print(dep.data)

# deleteDepestNode(newBT, dep)

# print("fuck you")

# preOrderTraversal(newBT)

def deleteNodeBT(rootNode, node):
    if not rootNode:
        return "not existing sht"
    else:
        customQueue = []
        customQueue.append(rootNode)
        while customQueue != []:
            root = customQueue.pop(0)
            if root.data == node:
                dNode = getDepestNode(rootNode)
                root.data = dNode.data
                deleteDepestNode(rootNode, dNode)
                return ("the node has been successfully deleted")
            if (root.leftChild is not None):
                customQueue.append(root.leftChild)
            
            if (root.rightChild is not None):
                customQueue.append(root.rightChild)
            
        return "failded"

# deleteNodeBT(newBT, "Hot")
# print("fuck")
# levelOrderTraversal(newBT)


