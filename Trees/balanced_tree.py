class Tree:
    def __init__(self, _node):
        self.root = _node

class Node:
    def __init__(self, _data, _left, _right):
        self.data = _data
        self.left = _left
        self.right = _right
        

def is_balanced(root, height):
    if root == None:
        return True
    
    lh = get_height(root.left)
    rh = get_height(root.right)

    left = is_balanced(root.left, lh)
    right = is_balanced(root.right, rh)

    if abs(lh - rh) <= 1:
        return left and right

    return False  

def get_height(node):
    if node.left!= None and node.right!=None:
        return 1 + max(get_height(node.left)  + get_height(node.right))
    elif node.left != None:
        return 1 + get_height(node.left)
    elif node.right != None:
        return 1 + get_height(node.right)
    return 1

    





def height(root):
    if root == None:
        return 1
    elif root.left != None and root.right != None:
        return 1 + max(height(root.left), height(root.right))
    elif root.left != None:
        return 1 + height(root.left)
    elif root.right != None:
        return 1 + height(root.right)

def check_balanced(tree):
    if tree == None:
        return True
    
    left_h = height(tree.left)
    right_h = height(tree.right)

    difference = abs(left_h - right_h)
    
    return difference <= 1
        