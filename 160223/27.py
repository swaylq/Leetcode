class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        i = 0
        while i <= length - 1:
            if nums[i] == val:
                for j in range(i, length - 1):
                    nums[j] = nums[j + 1]
                length -= 1
            else:
                i += 1
        return length

def test():
    s = Solution()
    print s.removeElement([1,2,3,1], 1)

test()