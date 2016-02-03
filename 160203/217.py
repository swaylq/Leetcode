class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict = {}
        for num in nums:
            if dict.has_key(num):
                return True
            else:
                dict[num] = 1
        return False