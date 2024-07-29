class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp=[[0]*len(matrix[0]) for _ in range(len(matrix))]
        sum=0
        for i in range(len(matrix)):
            dp[i][0]=matrix[i][0]
            sum+=dp[i][0]
       

        for i in range(1,len(matrix[0])):
            dp[0][i]=matrix[0][i]
            sum+=dp[0][i]
        
        
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[i])):
                if matrix[i][j]==0:
                    dp[i][j]=0
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1
                sum+=dp[i][j]
        return sum
        
        