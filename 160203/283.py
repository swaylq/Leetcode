class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num = 0
        total = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                total += 1
        while num < total:
            for i in range(0, len(nums)):
                if nums[i] == 0:
                    num += 1
                    for j in range(i, len(nums) - num):
                        nums[j] = nums[j + 1]
                    nums[len(nums) - num] = 0
                    break