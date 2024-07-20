class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        z=nums.index(max(nums))
        for i in range(len(nums)):
            if z!=i and nums[i]*2>nums[z]:
                return -1
        return z
        