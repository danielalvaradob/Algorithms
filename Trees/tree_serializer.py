from tree_node import TreeNode

def serialize_tree(root : TreeNode):
    """
    Encodes a tree to a single list.

    :type root: TreeNode
    :rtype: list<TreeNode>
    """

    tree_list = []
    queue = []
    queue.append(root)

    while queue != []:
        element = queue.pop(0)
        if element != None:
            tree_list.append(element.val)
            if element.left == None and element.right == None:
                continue
            queue.append(element.left)
            queue.append(element.right)
        else:
            tree_list.append(None)

            
    return tree_list


def deserialize_tree(tree_data : list):
    """
    Decodes your encoded data to tree.
    
    :type data: list
    :rtype: TreeNode
    """

    value = tree_data.pop(0)
    if value == [None]:
        return None

    root = TreeNode()
    root.val = value
    root.left = deserialize_tree(tree_data)
    root.right = deserialize_tree(tree_data)

    return root

