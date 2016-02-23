class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1, 1]
        list = [0 for x in range(0, rowIndex + 1)]
        list[0] = 1
        list[1] = rowIndex
        for i in range(2, rowIndex + 1):
            list[i] = list[i - 1] * (rowIndex - i + 1) / i
        return list

def test():
    s = Solution()
    print s.getRow(3)
    
test()
    