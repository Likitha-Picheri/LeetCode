class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max=-1
        for i in range(len(accounts)):
            sum=0
            for j in range(len(accounts[i])):
                sum+=accounts[i][j]
            if max<sum:
                max=sum
        return max
        