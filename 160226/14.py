class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: return ""
        i = -1
        same = True
        limit = True
        while same and limit:
            i += 1
            same = True
            limit = True
            last = None
            for j in range(0, len(strs)):
                if i < len(strs[j]):
                    if last and not last == strs[j][i]:
                        same = False
                        break
                    else:
                        last = strs[j][i]
                else:
                    limit = False
                    break
        if i == 0: return ""
        return strs[0][0:i]
        
def test():
    s = Solution()
    print s.longestCommonPrefix(["dasjkdjalkdjsa", "d"])
    
test()