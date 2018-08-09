# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        self.inorder(root, res)
        minval = sys.maxint
        for i in xrange(len(res) - 1):
            minval = min(minval, abs(res[i] - res[i + 1]))
        return minval

    def inorder(self, root, res):
        if root == None:
            return

        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)
        return

# If you want the minimum difference between the parent child instead of any 2 nodes then the below is the solution using BFS.
#         nextlevel = [root]
#         minval = sys.maxint
#         while len(nextlevel)!=0:
#             if nextlevel[0] != None:
#                 if nextlevel[0].left!=None and nextlevel[0].right!=None:
#                     # print "root val:"+str(nextlevel[0].val)
#                     # print "rootleft val:"+str(nextlevel[0].left.val)
#                     # print "rootright val:"+str(nextlevel[0].right.val)
#                     minval = min(minval, abs(nextlevel[0].val - nextlevel[0].left.val), abs(nextlevel[0].val-nextlevel[0].right.val))
#                     nextlevel.append(nextlevel[0].left)
#                     nextlevel.append(nextlevel[0].right)
#                     nextlevel.pop(0)
#                 if nextlevel[0].left == None and nextlevel[0].right != None:
#                     # print "root val:"+str(nextlevel[0].val)
#                     # print "rootleft val:"+str(nextlevel[0].left.val)
#                     # print "rootright val:"+str(nextlevel[0].right.val)
#                     minval = min(minval, abs(nextlevel[0].val-nextlevel[0].right.val))
#                     nextlevel.append(nextlevel[0].right)
#                     nextlevel.pop(0)
#                 if nextlevel[0].right == None and nextlevel[0].left != None:
#                     # print "root val:"+str(nextlevel[0].val)
#                     # print "rootleft val:"+str(nextlevel[0].left.val)
#                     # print "rootright val:"+str(nextlevel[0].right.val)
#                     minval = min(minval, abs(nextlevel[0].val-nextlevel[0].left.val))
#                     nextlevel.append(nextlevel[0].left)
#                     nextlevel.pop(0)
#                 if nextlevel[0].left==None and nextlevel[0].right==None:
#                     nextlevel.pop(0)
#             else:
#                 nextlevel.pop(0)
#             # print minval
#             # print nextlevel

#         return minval
