# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        nodes = [[root]]
        nextlevel = []
        count = 0
        flag = 0
        while len(nodes[0]) != 0:
            for i in xrange(len(nodes[0])):
                if nodes[0][i].left == None and nodes[0][i].right == None:
                    count += 1
                    flag = 1
                    break
                else:
                    if nodes[0][i].left != None:
                        nextlevel.append(nodes[0][i].left)
                    if nodes[0][i].right != None:
                        nextlevel.append(nodes[0][i].right)
            nodes.append(nextlevel)
            nextlevel = []
            nodes.pop(0)
            if flag == 1:
                return count
                break
            count += 1
        return count