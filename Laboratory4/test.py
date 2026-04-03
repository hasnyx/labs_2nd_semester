import unittest
import random
from red_black_priority_queue import RedBlackPriorityQueue

class TestRedBlackPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.q = RedBlackPriorityQueue()

    def _check_rb(self, q):
        """Verify the properties of the Red-Black Tree."""
        if q.root is q.NIL:
            return

        self.assertEqual(q.root.color, False, "Root must be BLACK")

        def check(node):
            if node is q.NIL:
                return 1 
            
            if node.color == True: 
                self.assertEqual(node.left.color, False, "Red node has a red left child")
                self.assertEqual(node.right.color, False, "Red node has a red right child")
            
            left_bh = check(node.left)
            right_bh = check(node.right)
            
            self.assertEqual(left_bh, right_bh, "Black height mismatch between branches")
            
            return left_bh + (1 if node.color == False else 0)

        check(q.root)

    def _check_order(self, q):
        """Verify the ordering logic: Left child >= parent, Right child < parent."""
        def check(node):
            if node is q.NIL:
                return
            if node.left is not q.NIL:
                self.assertLessEqual(node.priority, node.left.priority, "Left child priority is less than parent priority")
            if node.right is not q.NIL:
                self.assertGreater(node.priority, node.right.priority, "Right child priority is greater than or equal to parent priority")
            check(node.left)
            check(node.right)
        check(q.root)

    def test_enqueue_and_order(self):
        """Test if enqueued items maintain Red-Black properties and custom ordering."""
        priorities = [5, 15, 3, 20, 8, 15]
        for p in priorities:
            self.q.enqueue(f"val_{p}", p)
            self._check_rb(self.q)
        self._check_order(self.q)

    def test_dequeue_sorted_order(self):
        """Test if items are dequeued in descending order of priority."""
        for p in [10, 50, 20, 40, 30]:
            self.q.enqueue("task", p)
        
        results = []
        while True:
            try:
                _, prio = self.q.dequeue()
                results.append(prio)
            except IndexError:
                break
        
        self.assertEqual(results, [50, 40, 30, 20, 10], "Queue did not return items in correct priority order")

    def test_peek_empty(self):
        """Test that peeking at an empty queue raises an IndexError."""
        with self.assertRaises(IndexError):
            self.q.peek()

    def test_large_random(self):
        """Stress test with a large number of random priorities."""
        data = [random.randint(1, 1000) for _ in range(100)]
        for p in data:
            self.q.enqueue("x", p)
        
        self._check_rb(self.q)
        
        extracted = []
        for _ in range(100):
            extracted.append(self.q.dequeue()[1])
        
        self.assertEqual(extracted, sorted(data, reverse=True))

if __name__ == "__main__":
    unittest.main()