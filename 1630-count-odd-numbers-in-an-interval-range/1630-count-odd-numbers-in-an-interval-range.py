class Solution:
    def countOdds(self, low: int, high: int) -> int:
        n=(high-low)//2
        count=0
        if (low%2==1 or high%2==1):
            n=n+1
        return n
