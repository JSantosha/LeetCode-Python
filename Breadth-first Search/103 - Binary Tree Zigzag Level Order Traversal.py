# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
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
        result = []
        v = []
        flag = 0
        while len(nodes[0]) != 0:
            for i in xrange(len(nodes[0])):
                v.append(nodes[0][i].val)
                if nodes[0][i].left != None:
                    nextlevel.append(nodes[0][i].left)
                if nodes[0][i].right != None:
                    nextlevel.append(nodes[0][i].right)
            if flag == 0:
                flag = 1
                result.append(v)
            else:
                flag = 0
                result.append(v[::-1])

            nodes.append(nextlevel)
            nextlevel = []
            v = []
            nodes.pop(0)
        return result
