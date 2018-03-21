class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        result = 0
        for i in xrange(len(nums)):
            result = result ^ nums[i]

        return result