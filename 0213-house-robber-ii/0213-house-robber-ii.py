class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        dp1=[0]*(n-1)
        dp2=[0]*(n-1)
        for i in range(n-1):
            pick=nums[i]
            if i>1:
                pick+=dp1[i-2]
            non_pick=dp1[i-1]
            dp1[i]=max(pick,non_pick)
        for i in range(1,n):
            pick=nums[i]
            if i >2:
                pick+=dp2[i-2-1]
            non_pick=dp2[i-1-1]
            dp2[i-1]=max(pick,non_pick)
        return max(dp1[-1],dp2[-1])