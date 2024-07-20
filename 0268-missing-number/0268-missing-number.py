class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)==(1+nums[len(nums)-1]):
            return len(nums)
        elif nums[0]!=0:
            return 0
        else:
            t=len(nums)
            x=t*(t+1)//2
            z=x-sum(nums)
            return z
