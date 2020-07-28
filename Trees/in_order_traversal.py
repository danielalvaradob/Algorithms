from tree_node import TreeNode


class Solution:
    def inorderTraversal(self, root: TreeNode):
        if root == None:
            return 
        

        values = []

        self.inorderTraversal_helper(self, root, values)

        return values


    def inorderTraversal_helper(self, root: TreeNode, values: list):
        if root == None:
            return 


