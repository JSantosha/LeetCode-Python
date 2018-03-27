# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        result = self.symmetric(root, root)
        return result

    def symmetric(self, root1, root2):
        if root1 == None and root2 == None:
            return True

        if root1 and root2 and (root1.val == root2.val):
            return (self.symmetric(root1.left, root2.right) and self.symmetric(root1.right, root2.left))
        else:
            return False


