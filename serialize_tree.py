class TreeNode:
    def __init__(self, _data):
        self.data = _data
        self.left = None
        self.right = None



def serialize(root):
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    """
    tree_list = ''
    queue = []
    queue.append(root)

    while queue != []:
        element = queue.pop(0)
        if element != None:
            tree_list += str(element.data) + ','
            queue.append(element.left)
            queue.append(element.right)
        else:
            tree_list += 'None' + ','

            
    return tree_list

    

def deserialize(data):
    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: TreeNode
    """
    string_list = data.split(',')
    print(string_list)
    root = deserialize_helper(string_list)
    return root


def deserialize_helper(sub_list):
    
    value = sub_list.pop(0)
    if value == 'None':
        return None

    root = Node(value)
    root.left = deserialize_helper(sub_list)
    root.right = deserialize_helper(sub_list)


if __name__ == "__main__":
    root = Node(1)

    node2 = Node(2)
    node7 = Node(7)

    node4 = Node(4)
    node5 = Node(5)

    node8 = Node(8)


    root.left = node2
    root.right = node7

    node2.left = node4
    node2.right = node5


    node7.right = node8

    s = serialize(root)

    print(s)
    print(deserialize(s))


    