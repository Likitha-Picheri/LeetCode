class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:

        ans=set()
        current=set()
        for x in arr:
            current={x| i for i in current}
            current.add(x)
            ans|=current
        return len(ans)

        # t=len(arr)
        # dp=[[0]*t for i in range(t)]
        # for i in range(t):
        #     for j in range(i,t):
        #         if i==j:
        #             dp[i][j]=arr[i]
        #         else:
        #             dp[i][j]=dp[i][j-1]|arr[j]
        # print(dp)
        # return 10
        
        