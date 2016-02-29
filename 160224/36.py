class Solution(object):
    def isValidLine(self, x):
        dict = {}
        for i in range(0, 9):
            c = self.board[x][i]
            if c != '.':
                if c >= '1' and c <= '9':
                    if dict.has_key(c):
                        return False
                    else:
                        dict[c] = True
                else:
                    return False
        return True
        
    def isValidColumn(self, x):
        dict = {}
        for i in range(0, 9):
            c = self.board[i][x]
            if c != '.':
                if c >= '1' and c <= '9':
                    if dict.has_key(c):
                        return False
                    else:
                        dict[c] = True
                else:
                    return False
        return True
        
    def isValidRec(self, x):
        dict = {}
        for i in range((x / 3) * 3, (x / 3) * 3 + 3):
            for j in range((x % 3) * 3, (x % 3) * 3 + 3):
                c = self.board[i][j]
                if c != '.':
                    if c >= '1' and c <= '9':
                        if dict.has_key(c):
                            return False
                        else:
                            dict[c] = True
                    else:
                        return False
        return True
        
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        self.board = board
        for i in range(0, 9):
            if not (self.isValidLine(i) and self.isValidColumn(i) and self.isValidRec(i)):
                return False
        return True
        
def test():
    s = Solution()
    list = [['0' for x in range(0, 9)] for y in range(0, 9)]
    print s.isValidSudoku(list)
    
test()
        