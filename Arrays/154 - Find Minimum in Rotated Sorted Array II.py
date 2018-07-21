class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums[0], nums[1])
        pivotelem = self.findpivot(nums, 0, len(nums) - 1)
        if pivotelem == -1:
            return nums[0]
        else:
            return nums[pivotelem + 1]

    def findpivot(self, nums, start, end):
        if end < start:
            return -1
        mid = int((start + end) / 2)
        print mid

        if mid < end and nums[mid + 1] < nums[mid]:
            return mid
        if mid > start and nums[mid - 1] > nums[mid]:
            return mid - 1
        if nums[start] > nums[mid]:
            return self.findpivot(nums, start, mid - 1)
        if nums[start] < nums[mid]:
            return self.findpivot(nums, mid + 1, end)
        if nums[start] == nums[mid]:
            return max(self.findpivot(nums, start, mid - 1), self.findpivot(nums, mid + 1, end))
