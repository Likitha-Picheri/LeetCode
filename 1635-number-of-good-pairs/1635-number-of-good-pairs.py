class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        sum1=0
        for i in range(len(nums)):
            if nums[i] in nums[i+1:]:
                count=nums[i+1:].count(nums[i])
                print(nums[i])
                sum1+=count
        return sum1
        