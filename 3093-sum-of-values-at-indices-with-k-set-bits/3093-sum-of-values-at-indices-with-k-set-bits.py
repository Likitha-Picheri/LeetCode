class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        sum=0
        for i in range(len(nums)):
            t=str(bin(i))
            y=t.count("1")
            if y==k:
                sum+=nums[i]
        return sum
        