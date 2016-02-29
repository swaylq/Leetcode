import math
class Solution(object):
    def isPrime(self, x):
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True
    
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # find the small primes
        self.list = []
        for i in range(2, int(math.sqrt(n)) + 1):
            if self.isPrime(i):
                self.list.append(i)
        self.arr = [True for x in range(0, n)]
        for i in range(0, len(self.list)):
            k = self.list[i]
            j = 2 * k
            while j < n:
                self.arr[j] = False
                j += k
        result = 0
        for i in range(2, n):
            if self.arr[i]:
                result += 1
        return result
        
def test():
    s = Solution()
    n = input()
    print s.countPrimes(n)
    
    
test()
