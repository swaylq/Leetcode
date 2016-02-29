class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        origin = x
        reserve = 0
        while x > 0:
            reserve *= 10
            reserve += x % 10
            x = x / 10
        return reserve == origin
        
def test():
    s = Solution()
    n = input()
    print s.isPalindrome(n)
    
test()
