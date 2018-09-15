# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        start = 0
        end = len(nums) - 1
        root = self.constructMaxtree(nums, start, end)
        return root

    def constructMaxtree(self, array, start, end):
        if start > end:
            return None

        if start == end:
            return TreeNode(array[start])
        maxval = -sys.maxint - 1
        index = 0
        for i in xrange(start, end + 1):
            if array[i] > maxval:
                maxval = array[i]
                index = i
        root = TreeNode(array[index])
        if index == 0:
            root.left = None
        else:
            root.left = self.constructMaxtree(array, start, index - 1)
        if index == end:
            root.right = None
        else:
            root.right = self.constructMaxtree(array, index + 1, end)
        return root
