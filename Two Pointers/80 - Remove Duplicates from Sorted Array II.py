class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        prev = nums[0]
        count = 1
        j = 1
        numelements = 0
        for i in xrange(1, len(nums)):
            if j < len(nums):
                if nums[j] == prev:
                    if count >= 2:
                        t = j
                        x = nums.pop(j)
                        nums.append(x)
                        numelements += 1
                        j = t
                    else:
                        count += 1
                        j += 1
                else:
                    if i == len(nums):
                        break
                    count = 1
                    prev = nums[j]
                    j += 1
        return len(nums) - numelements
