class Solution:
    def rob(self, nums: List[int]) -> int:
        t=len(nums)
        dp=[0]*t
        for i in range(t):
            pick=nums[i]
            if i>1:
                pick+=dp[i-2]
            non_pick=dp[i-1]
            dp[i]=max(pick,non_pick)
        print(dp)
        return dp[t-1]

        