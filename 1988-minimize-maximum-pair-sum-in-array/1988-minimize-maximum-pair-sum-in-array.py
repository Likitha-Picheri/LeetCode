class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        t=len(nums)-1
        max=0
        for i in range(len(nums)//2):
            sum=nums[i]+nums[t-i]
            if max<sum:
                max=sum
        return max

