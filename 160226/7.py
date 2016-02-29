class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        n = abs(x)
        while n > 0:
            result *= 10
            result += n % 10
            n = n / 10
        if result > 2147483648: return 0
        if x >= 0: return result
        else: return -result

def test():
    s = Solution()
    print s.reverse(1563847412)
    
test()
            