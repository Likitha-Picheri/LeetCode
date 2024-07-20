class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        z=nums.index(max(nums))
        nums.sort()
        t=len(nums)
        for i in range(t-1):
            if 2*nums[i]>nums[t-1]:
                return -1
        return z
        