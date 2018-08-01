class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sumval = -sys.maxint - 1
        result = 0
        for i in xrange(len(nums)):
            result += nums[i]
            print sumval
            sumval = max(sumval,result)
            if result > sumval:
                sumval = result
            if result < 0:
                result = 0
        return sumval