class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        y=set(nums)
        nums.clear()
        for i in y:
            nums.append(i)
        nums.sort()
        return len(nums)