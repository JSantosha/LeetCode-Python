# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s == None and t == None:
            return True
        if (s == None and t != None) or (s != None and t == None):
            return False
        return self.recurparent(s, t)

    def recurparent(self, s, t):
        if s == None and t == None:
            return True
        if (s == None and t != None) or (s != None and t == None):
            return False
        if t.val == s.val:
            if self.recurchild(s.left, t.left) and self.recurchild(s.right, t.right):
                return True
            else:
                return False or (self.recurparent(s.left, t) or self.recurparent(s.right, t))
        else:
            return False or (self.recurparent(s.left, t) or self.recurparent(s.right, t))

    def recurchild(self, s, t):
        if s == None and t == None:
            return True
        if (s == None and t != None) or (s != None and t == None):
            return False
        if s.val == t.val:
            return True and self.recurchild(s.left, t.left) and self.recurchild(s.right, t.right)
        else:
            return False


