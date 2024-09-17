import unittest
from q2_stackMin import Stack, Node



class TestStack(unittest.TestCase):

    def test_push(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        stack.push(30)
        print(stack)
        self.assertEqual(str(stack), "10\n20\n30")

    def test_isEmpty(self):
        stack = Stack()
        self.assertTrue(stack.isEmpty())
        stack.push(10)
        self.assertFalse(stack.isEmpty())

    def test_push_and_isEmpty(self):
        stack = Stack()
        self.assertTrue(stack.isEmpty())
        stack.push(10)
        self.assertFalse(stack.isEmpty())
        stack.push(20)
        self.assertEqual(str(stack), "10\n20")

if __name__ == '__main__':
    unittest.main()
