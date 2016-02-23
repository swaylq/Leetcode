class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        length = len(nums)
        if length == 0: return 0
        while i < length - 1:
            i += 1
            if nums[i] > nums[j]:
                j += 1
                nums[j] = nums[i]
        return j + 1
def test():
    s = Solution()
    nums = [1, 1, 1, 2]
    print s.removeDuplicates(nums)
    
test()