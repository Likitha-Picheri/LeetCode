class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prices=prices[0]
        max_profit=0
        for price in prices:
            min_prices=min(price,min_prices)
            max_profit=max(max_profit,price-min_prices)
            
        return max_profit
        
        
