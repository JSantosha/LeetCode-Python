class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if k > len(nums):
            return 0
        if k == 1:
            return max(nums) / float(k)
        sumval = 0
        for i in xrange(k):
            sumval += nums[i]
        resultval = sumval
        for i in xrange(k, len(nums)):
            sumval = sumval - nums[i - k] + nums[i]
            resultval = max(sumval, resultval)

        return resultval / float(k)