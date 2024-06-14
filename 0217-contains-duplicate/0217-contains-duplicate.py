class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        y=set(nums)
        t=list(y)
        if len(t)==len(nums):
            return False
        else:
            return True