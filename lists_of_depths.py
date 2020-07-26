def lists_depths_aux(root, lists, level):
    if (root == None):
        return
    if len(lists) == level:
        # create list
        new_list = []
        lists.append(new_list)
    else:
        new_list = lists[level]
    
    new_list.append(root)
    lists_depths_aux(root.left, lists, level +1)
    lists_depths_aux(root.right, lists, level +1)


def lists_depths(root):
    lists = []
    lists_depths_aux(root, lists, 0)
    return lists



