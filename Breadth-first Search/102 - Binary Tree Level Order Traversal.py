# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [[root.val]]
        nodes = [[root]]
        nextlevel = []
        resultvalues = []
        v = []
        while len(nodes[0]) != 0:
            for i in xrange(len(nodes[0])):
                v.append(nodes[0][i].val)
                if nodes[0][i].left != None:
                    nextlevel.append(nodes[0][i].left)
                if nodes[0][i].right != None:
                    nextlevel.append(nodes[0][i].right)

            nodes.append(nextlevel)
            nodes.pop(0)
            nextlevel = []
            resultvalues.append(v)
            v = []

        return resultvalues