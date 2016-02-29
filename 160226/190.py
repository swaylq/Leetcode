class Solution(object):
    def decToBit(self, x):
        list = [0 for i in range(0, 32)]
        j = 31
        while x > 0:
            list[j] = x % 2
            x = x / 2
            j -= 1
        return list
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        list = self.decToBit(n)
        result = 0
        temp = 1
        for i in range(0, 32):
            result += list[i] * temp
            temp *= 2
        return result

def test():
    s = Solution()
    print s.reverseBits(43261596)
    
test()