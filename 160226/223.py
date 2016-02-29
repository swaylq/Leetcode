class Solution(object):
    def coverLineLength(self, a, b, c, d):
        head = max(a, c)
        trail = min(b, d)
        return trail - head if trail - head > 0 else 0
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        areaOne = (C - A) * (D - B)
        areaTwo = (G - E) * (H - F)
        return areaOne + areaTwo - self.coverLineLength(A, C, E, G) * self.coverLineLength(B, D, F, H)
        
def test():
    s = Solution()
    print s.computeArea(0, 0, 0, 0, -1, -1, 1, 1)
    
test()