class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        temp = 0
        for i in xrange(len(nums)):
            if nums[i] == 0:
                temp = 0
            else:
                temp += 1
                result = max(temp, result)

        return result