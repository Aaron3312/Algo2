# Middle of the Linked List
# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
class Solution(object):
    def middleNode(self, head):
        count = 0
        dummy = head
        while dummy is not None:
            count += 1
            dummy = dummy.next
        print(count)
        dummy = head
        if count % 2 == 0:
            for _ in range(count // 2):
                dummy = dummy.next
        else:
            for _ in range(count // 2 ):
                dummy = dummy.next    
        return (dummy)
        


# Función para crear una lista enlazada desde un array
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Función para probar la función middleNode
def test_middle_node(arr):
    # Crear la lista enlazada desde el array dado
    head = create_linked_list(arr)
    
    # Instanciar la clase Solution y probar la función
    solution = Solution()
    result = solution.middleNode(head)
    
    # Mostrar el resultado
    print(f"El nodo del medio de la lista {arr} es: {result}")

# Pruebas
test_middle_node([1, 2, 3, 4, 5])  # Debería devolver 3
test_middle_node([1, 2, 3, 4, 5, 6])  # Debería devolver 4
test_middle_node([1])  # Debería devolver 1