class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in range(0, len(s)):
            rank = 1
            for k in range(i, len(s) - 1):
                rank *= 26
            result += rank * (ord(s[i]) - 64)
            
        return result