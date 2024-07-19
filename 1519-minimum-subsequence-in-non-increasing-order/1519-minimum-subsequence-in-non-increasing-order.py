class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        sum1=sum(nums)
        temp=0
        i=len(nums)-1
        while i>0:
            sum1=sum1-nums[i]
            temp=temp+nums[i]
            if sum1<temp:
                t=nums[i:]
                return t[::-1]
            i-=1
        t=nums[i:]
        return t[::-1]

        
        