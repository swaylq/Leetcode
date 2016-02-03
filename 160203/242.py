class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sDict = {}
        tDict = {}
        for i in s:
            sDict[i] = sDict.get(i, 0) + 1
        for i in t:
            tDict[i] = tDict.get(i, 0) + 1
        return sDict == tDict