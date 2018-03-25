class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = 0
        for i in xrange(len(nums)):
            res = res ^ nums[i]

        n1 = 0
        n2 = 0
        x = res & ~(res - 1)
        for i in xrange(len(nums)):
            if x & nums[i] > 0:
                n1 = n1 ^ nums[i]
            else:
                n2 = n2 ^ nums[i]

        return [n1, n2]
