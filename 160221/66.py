class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        digits[length - 1] += 1
        for i in range(length - 1, -1, -1):
            if digits[i] >= 10:
                digits[i] = digits[i] % 10
                if i == 0:
                    digits.append(digits[length - 1])
                    for j in range(length - 1, 0, -1):
                        digits[j] = digits[j - 1]
                    digits[0] = 1
                else:
                    digits[i - 1] += 1
        return digits
def test():
    s = Solution()
    d = [9,9,9,9,8]
    print s.plusOne(d)
    
test()