class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0: return []
        list = [[1]]
        for i in range(1, numRows):
            line = [0 for x in range(0, i + 1)]
            line[0] = list[i - 1][0]
            line[i] = list[i - 1][i - 1]
            for j in range(1, i):
                line[j] = list[i - 1][j - 1] + list[i - 1][j]
            list.append(line)
        return list
    

def test():
    s = Solution()
    print s.generate(5)
    
test()