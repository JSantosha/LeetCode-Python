class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) * len(nums[0]) != r * c:
            return nums

        newlist = []
        x = 0
        y = 0
        for i in xrange(r):
            newrow = []
            for j in xrange(c):
                newrow.append(nums[x][y])
                y += 1
                if y == len(nums[0]):
                    y = 0
                    x += 1
            newlist.append(newrow)

        return newlist