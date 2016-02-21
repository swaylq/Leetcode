def findAll():
    list = []
    i = 1
    while i < 100000000000:
        list.append(i)
        i *= 3
    print list

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        list = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721, 129140163, 387420489, 1162261467, 3486784401, 10460353203, 31381059609, 94143178827]
        return n in list

def test():
    findAll()
    s = Solution()
    print s.isPowerOfThree(81)
    
test()