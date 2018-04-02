class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        length = len(findNums)
        lengtharr = len(nums) - 1
        for i in xrange(length):
            j = lengtharr
            x = -1
            while j >= 0:
                if nums[j] == findNums[i]:
                    result.append(x)
                    break
                if nums[j] > findNums[i]:
                    x = nums[j]
                j -= 1

        return result