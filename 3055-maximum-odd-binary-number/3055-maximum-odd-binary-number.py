class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        one=s.count('1')-1
        zero=s.count('0')
        t='1'*(one) + '0'*zero
        t=t+'1'
        print(t)
        return t
        