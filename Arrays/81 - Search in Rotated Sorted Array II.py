class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        if len(nums) == 1 and target == nums[0]:
            return True
        if len(nums) == 1 and target != nums[0]:
            return False
        pivotelem = self.findpivot(nums, 0, len(nums) - 1)
        # print pivotelem
        print pivotelem
        if pivotelem != -1:
            if nums[pivotelem] == target:
                return True
            if target < nums[0]:
                return self.findelem(nums, pivotelem + 1, len(nums) - 1, target)
            return self.findelem(nums, 0, pivotelem, target)
        else:
            return self.findelem(nums, 0, len(nums) - 1, target)

    def findelem(self, nums, start, end, target):
        if end < start:
            return False

        mid = int((start + end) / 2)
        if nums[mid] == target:
            return True
        if target < nums[mid]:
            return self.findelem(nums, start, mid - 1, target)
        if target > nums[mid]:
            return self.findelem(nums, mid + 1, end, target)

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

