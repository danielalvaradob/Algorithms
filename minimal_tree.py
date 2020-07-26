

def minimal_tree(array, node):
    # get element in the middle
    middle_e = array[ len(array)//2 ]

    left_a = array[:middle_e]
    right_a = array[middle_e:]
    
    if node == None:
        node.value = middle_e
    minimal_tree(left_a, node.left)
    minimal_tree(right_a, node.right)
    