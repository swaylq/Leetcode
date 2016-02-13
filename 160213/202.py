class Solution(object):
    def getNext(self, n):
        result = 0
        while n > 0:
            m = n % 10
            n = n / 10
            result += m * m
        return result
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dict = {}
        while (not dict.has_key(n)) and (not n == 1):
            dict[n] = True
            n = self.getNext(n)
        return n == 1
    
def test():
    s = Solution()
    print s.isHappy(4)
    
test()