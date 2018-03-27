# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return root.val
        nodes = [[root]]
        nextlevel = []
        resultvalue = []
        v = []
        while len(nodes[0]) != 0:
            for i in xrange(len(nodes[0])):
                v.append(nodes[0][i].val)
                if nodes[0][i].left != None:
                    nextlevel.append(nodes[0][i].left)
                if nodes[0][i].right != None:
                    nextlevel.append(nodes[0][i].right)

            resultvalue.append(v)
            nodes.append(nextlevel)
            nextlevel = []
            v = []
            nodes.pop(0)
        return resultvalue[len(resultvalue) - 1][0]