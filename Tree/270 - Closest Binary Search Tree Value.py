# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        res = []
        self.inorder(root, res)
        temp = res[0]
        minval = abs(target - res[0])
        for i in xrange(1, len(res)):
            if abs(res[i] - target) < minval:
                minval = abs(res[i] - target)
                temp = res[i]
        return temp

    def inorder(self, root, res):
        if root == None:
            return
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)
