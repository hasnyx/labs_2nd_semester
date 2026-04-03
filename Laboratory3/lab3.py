class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def binary_tree_diameter(tree: BinaryTree) -> int:
    max_dia = 0

    def get_height(node):
        nonlocal max_dia
        if not node:
            return -1
        
        if not node.left and not node.right:
            return 0
        
        left_h = get_height(node.left)
        right_h = get_height(node.right)
        
        if node.left is not None and node.right is not None:
            current_diameter = left_h + right_h + 2
            max_dia = max(max_dia, current_diameter)
            
        return 1 + max(left_h, right_h)

    if not tree:
        return 0
        
    get_height(tree)
    return max_dia

def print_tree_structure():
    structure = r"""
    Візуалізація дерева з умови:
              1
             / \
            3   2
           / \
          7   4
         /     \
        8       5
       /         \
      9           6
    """
    print(structure)

if __name__ == "__main__":
    node9 = BinaryTree(9)
    node8 = BinaryTree(8, left=node9)
    node7 = BinaryTree(7, left=node8)
    node6 = BinaryTree(6)
    node5 = BinaryTree(5, right=node6)
    node4 = BinaryTree(4, right=node5)
    node3 = BinaryTree(3, left=node7, right=node4)
    node2 = BinaryTree(2)
    root = BinaryTree(1, left=node3, right=node2)

    print_tree_structure()
    
    diameter = binary_tree_diameter(root)
    
    print("-" * 60)
    print(f"The maximum diameter of the binary tree is: {diameter}")
    print("Longest path: 9 -> 8 -> 7 -> 3 -> 4 -> 5 -> 6")
    print(f"To travel from leaf 9 to leaf 6, you must cross {diameter} edges.")
    print("-" * 60)
