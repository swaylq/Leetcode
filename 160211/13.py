class Solution(object):
    def romanToInt(self, s):
        value= {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        result = 0
        left = 0
        for c in s:
            if left < value[c]:
                result = result - 2 * left
            result = result + value[c]
            left = value[c]
        return result
        
def test():
    s = Solution()
    print s.romanToInt('IV')

test()