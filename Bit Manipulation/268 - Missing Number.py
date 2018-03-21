class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = min(nums)
        y = max(nums)
        sum1 = 0
        sum2 = 0
        for i in xrange(x, y + 1):
            sum1 += i

        for i in nums:
            sum2 += i

        if sum2 == sum1:
            if x - 1 >= 0:
                return x - 1
            else:
                return y + 1

        return sum1 - sum2