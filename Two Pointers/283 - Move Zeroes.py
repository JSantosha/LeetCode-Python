class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = nums.count(0)
        t = count
        if count != 0:
            i = 0
            while t>0:
                nums.remove(0)
                t-=1

            while count>0:
                nums.append(0)
                count-=1
