import unittest
from lab3 import BinaryTree, binary_tree_diameter

class TestBinaryTreeDiameter(unittest.TestCase):

    def test_empty_tree(self):
        """EMPTY TREE: What if the tree is missing? Should be 0."""
        self.assertEqual(binary_tree_diameter(None), 0)

    def test_single_node(self):
        """SINGLE NODE: One root is one leaf. No pair exists. Should be 0."""
        root = BinaryTree(1)
        self.assertEqual(binary_tree_diameter(root), 0)

    def test_bamboo_tree(self):
        """BAMBOO: Line-shaped tree (1 -> 2 -> 3). Only one leaf exists. Should be 0."""
        root = BinaryTree(1, left=BinaryTree(2, left=BinaryTree(3)))
        self.assertEqual(binary_tree_diameter(root), 0)

    def test_simple_y_shape(self):
        """MINIMAL PAIR: Root and two leaves. Path: leaf-root-leaf. Should be 2."""
        root = BinaryTree(1, left=BinaryTree(2), right=BinaryTree(3))
        self.assertEqual(binary_tree_diameter(root), 2)

    def test_provided_example(self):
        """CLASSIC: The specific tree from your diagram. Should be 6."""
        node9 = BinaryTree(9)
        node8 = BinaryTree(8, left=node9)
        node7 = BinaryTree(7, left=node8)
        node6 = BinaryTree(6)
        node5 = BinaryTree(5, right=node6)
        node4 = BinaryTree(4, right=node5)
        node3 = BinaryTree(3, left=node7, right=node4)
        node2 = BinaryTree(2)
        root = BinaryTree(1, left=node3, right=node2)
        
        self.assertEqual(binary_tree_diameter(root), 6)

    def test_diameter_not_through_root(self):
        """DEEP DIAMETER: Path does not pass through the main root."""
        left_branch = BinaryTree(3, left=BinaryTree(5, left=BinaryTree(7)))
        right_branch = BinaryTree(4, right=BinaryTree(6, right=BinaryTree(8)))
        sub_root = BinaryTree(2, left=left_branch, right=right_branch)
        root = BinaryTree(1, left=sub_root)
        
        self.assertEqual(binary_tree_diameter(root), 6)

    def test_unbalanced_tree(self):
        """UNBALANCED TREE: Checking for the correct max_diameter selection."""
        node4 = BinaryTree(4, left=BinaryTree(5), right=BinaryTree(6))
        node2 = BinaryTree(2, left=node4)
        root = BinaryTree(1, left=node2, right=BinaryTree(3))
        
        self.assertEqual(binary_tree_diameter(root), 4)

if __name__ == "__main__":
    unittest.main()
