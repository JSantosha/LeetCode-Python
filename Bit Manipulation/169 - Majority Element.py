class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in xrange(len(nums)):
            if dic.get(nums[i], 0) != 0:
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1

        for k, v in dic.iteritems():
            if v > len(nums) / 2:
                return k
