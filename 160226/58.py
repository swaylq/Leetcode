class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        i = len(s) - 1
        while i >= 0 and s[i] == ' ': i-=1
        while i >= 0:
            if s[i] == ' ': return length
            else: length += 1
            i -= 1
        return length
            
        
def test():
    s = Solution()
    print s.lengthOfLastWord("a ")
    
test()