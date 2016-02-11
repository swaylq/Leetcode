class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for i in range(0, len(nums)):
            dict[nums[i]] = dict.get(nums[i], 0) + 1
            if dict[nums[i]] > len(nums) / 2:
                return nums[i]