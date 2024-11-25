class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1
    


def minValueNode(bstNode):
    current = bstNode
    while current.leftChild is not None:
        current = current.leftChild
    return current
    

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




newBs = BSTNode(10)



