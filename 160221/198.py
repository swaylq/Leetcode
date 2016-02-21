class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0: return 0
        arr = [[0 for x in range(0, 2)] for y in range(0, length)]
        arr[0] = [0, nums[0]]
        for i in range(1, length):
            arr[i][0] = max(arr[i - 1][0], arr[i - 1][1])
            arr[i][1] = arr[i - 1][0] + nums[i]
        return max(arr[length - 1][0], arr[length - 1][1])

def test():
    s = Solution()
    list = [1, 2, 3, 4]
    print s.rob(list)
    
test()