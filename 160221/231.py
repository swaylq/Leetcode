class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n % 2 == 0 and n > 0:
            n = n / 2
        return n == 1
        
def test():
    s = Solution()
    print s.isPowerOfTwo(3)

test()