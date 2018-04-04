# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root == None:
            return []
        self.inorderlist(root, result)
        return result

    def inorderlist(self, root, result):

        if root == None:
            return None
        if root.left != None:
            self.inorderlist(root.left, result)
        result.append(root.val)
        if root.right != None:
            self.inorderlist(root.right, result)