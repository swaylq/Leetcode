class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while not (n == 0):
            if (n % 2) == 1:
                result += 1
            n = n / 2
        return result
    
    
def test():
    s = Solution()
    print s.hammingWeight(11)

test()