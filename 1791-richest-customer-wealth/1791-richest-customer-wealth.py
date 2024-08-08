class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max=-1
        for i in range(len(accounts)):
            sum1=sum(accounts[i])
            if max<sum1:
                max=sum1
        return max