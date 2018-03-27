# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    result = []

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [[root.val]]
        l = []
        t = [[root]]
        v = []
        nextlevel = []

        while len(t[0]) != 0:
            for i in xrange(len(t[0])):
                v.append(t[0][i].val)
                if t[0][i].left != None:
                    nextlevel.append(t[0][i].left)
                if t[0][i].right != None:
                    nextlevel.append(t[0][i].right)
            t.append(nextlevel)
            nextlevel = []
            t.pop(0)
            l.append(v)
            v = []
        return l[::-1]
