
# Palindrome Linked List
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.




class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        # TODO
        counter = 0
        dummy = ListNode(0)
        dummy.next = head
        mano = dummy.next
        lsd = []
       
        while mano is not None:
            counter += 1
            mano = mano.next
        mano = dummy.next
        if counter % 2 == 0:
            for _ in range((counter // 2)):
                lsd.append(mano.val)
                mano = mano.next
            isa = (len(lsd)-1)
            while mano is not None:
                if mano.val != lsd[isa]:
                    return False
                mano = mano.next
                isa -= 1
        else:
            for _ in range ((counter//2)+1):
                lsd.append(mano.val)
                # print(mano.val)
                mano = mano.next
            print(lsd)
            isa = (len(lsd)-2)
            while mano is not None:
                if mano.val != lsd[isa]:
                    return False
                mano = mano.next
                isa -= 1
        return True


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

# Función para probar si una lista enlazada es un palíndromo
def test_is_palindrome(arr):
    # Crear la lista enlazada desde el array dado
    head = create_linked_list(arr)
    
    # Instanciar la clase Solution y probar la función
    solution = Solution()
    result = solution.isPalindrome(head)
    
    # Mostrar el resultado
    print(f"La lista {arr} es un palíndromo: {result}")

# Pruebas
test_is_palindrome([1, 2, 2, 1])  # Debería devolver True
test_is_palindrome([1, 2, 3, 2, 1])  # Debería devolver True
test_is_palindrome([1, 2])  # Debería devolver False
test_is_palindrome([1, 2, 3])  # Debería devolver False