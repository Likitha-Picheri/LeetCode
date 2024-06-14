class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        k=0
        for i in range(1,n):
            if prices[i]>prices[i-1]:
                k+=prices[i]-prices[i-1]
        return k
        