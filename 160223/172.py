class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n > 0:
            result += n / 5
            n = n / 5
        return result
        
def test():
    s = Solution()
    n = input()
    print s.trailingZeroes(n)
    
test()