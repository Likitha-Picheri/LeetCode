class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if i!=nums[i]:
                return i
        return len(nums)
        # if len(nums)==(1+nums[len(nums)-1]):
        #     return len(nums)
        # else:
        #     t=len(nums)
        #     x=t*(t+1)//2
        #     z=x-sum(nums)
        #     return z
