from tree_serializer import *


if __name__ == "__main__":

    # Tree
    root = TreeNode()
    root.val = 1
    left1 = TreeNode()
    left1.val = 2
    right1 = TreeNode()
    right1.val = 3

    root.left = left1
    root.right = right1
    
    left12 = TreeNode()
    left12.val = 4
    left1.left = left12

    left_r = TreeNode()
    left_r.val = 5
    right_r = TreeNode()
    right_r.val = 6

    right1.left = left_r
    right1.right = right_r
    

    tree_serialized = serialize_tree(root)
    print(tree_serialized)
    