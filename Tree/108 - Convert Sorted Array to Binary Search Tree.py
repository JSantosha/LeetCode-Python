# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.height = 1
#
# AVL tree implementation.
#
# class Solution(object):
#     def sortedArrayToBST(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: TreeNode
#         """
#         if len(nums) == 0:
#             return None
#
#         root = None
#         for i in xrange(len(nums)):
#             root = self.buildtree(root, nums[i])
#         self.inorder(root)
#         return root
#
#     def inorder(self, root):
#         if root == None:
#             return
#
#         self.inorder(root.left)
#         print root.val
#         self.inorder(root.right)
#
#         return
#
#     def buildtree(self, root, key):
#         if root == None:
#             return TreeNode(key)
#
#         if key > root.val:
#             root.right = self.buildtree(root.right, key)
#
#         if key < root.val:
#             root.left = self.buildtree(root.left, key)
#
#         root.height = 1 + max(self.getheight(root.left), self.getheight(root.right))
#
#         balance = self.balance(root)
#         if balance > 1 and key < root.left.val:
#             return self.rightRotate(root)
#
#         if balance < -1 and key > root.right.val:
#             return self.leftRotate(root)
#
#         if balance > 1 and key > root.left.val:
#             root.left = self.leftRotate(root.left)
#             return self.rightRotate(root)
#
#         if balance < -1 and key < root.right.val:
#             root.right = self.rightRotate(root.right)
#             return self.leftRotate(root)
#
#         return root
#
#     def rightRotate(self, root):
#         if root == None:
#             return None
#
#         temp = root.left
#         temp2 = temp.right
#         temp.right = root
#         root.left = temp2
#
#         temp.height = 1 + max(self.getheight(temp.left), self.getheight(temp.right))
#         root.height = 1 + max(self.getheight(root.left), self.getheight(root.right))
#
#         return temp
#
#     def leftRotate(self, root):
#
#         temp = root.right
#         temp2 = temp.left
#
#         root.right = temp2
#         temp.left = root
#         temp.height = 1 + max(self.getheight(temp.left), self.getheight(temp.right))
#         root.height = 1 + max(self.getheight(root.left), self.getheight(root.right))
#
#         return temp
#
#     def getheight(self, root):
#         if root == None:
#             return 0
#         return root.height
#
#     def balance(self, root):
#         if root == None:
#             return 0
#
#         return self.getheight(root.left) - self.getheight(root.right)
#
#
# s = Solution()
# s.sortedArrayToBST([-10,-3,0,5,9])

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        mid = int(len(nums) / 2)
        root = TreeNode(nums[mid])
        print nums[mid]
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root
