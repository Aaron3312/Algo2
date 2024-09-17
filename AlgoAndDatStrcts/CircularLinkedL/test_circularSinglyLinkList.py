import unittest
from circularSinglyLinkList import CSLinkedList, Node

class TestCSLinkedList(unittest.TestCase):

    def test_append(self):
        csll = CSLinkedList()
        csll.append(1)
        csll.append(2)
        csll.append(3)
        self.assertEqual(str(csll), "1 -> 2 -> 3")
        self.assertEqual(csll.head.value, 1)
        self.assertEqual(csll.tail.value, 3)
        self.assertEqual(csll.tail.next, csll.head)
        self.assertEqual(csll.length, 3)

    def test_prepend(self):
        csll = CSLinkedList()
        csll.prepend(1)
        csll.prepend(2)
        csll.prepend(3)
        self.assertEqual(str(csll), "3 -> 2 -> 1")
        self.assertEqual(csll.head.value, 3)
        self.assertEqual(csll.tail.value, 1)
        self.assertEqual(csll.tail.next, csll.head)
        self.assertEqual(csll.length, 3)

    def test_append_and_prepend(self):
        csll = CSLinkedList()
        csll.append(1)
        csll.prepend(2)
        csll.append(3)
        csll.prepend(4)
        self.assertEqual(str(csll), "4 -> 2 -> 1 -> 3")
        self.assertEqual(csll.head.value, 4)
        self.assertEqual(csll.tail.value, 3)
        self.assertEqual(csll.tail.next, csll.head)
        self.assertEqual(csll.length, 4)

    def test_empty_list(self):
        csll = CSLinkedList()
        self.assertEqual(str(csll), "")
        self.assertIsNone(csll.head)
        self.assertIsNone(csll.tail)
        self.assertEqual(csll.length, 0)

if __name__ == '__main__':
    unittest.main()