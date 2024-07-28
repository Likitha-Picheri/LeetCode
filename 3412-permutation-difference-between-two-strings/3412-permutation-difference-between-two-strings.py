class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        sum=0
        for i in range(len(s)):
            j=t.index(s[i])
            sum+=abs(i-j)
        return sum
        