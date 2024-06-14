class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        s=set(nums)
        t=list(s)
        y=nums.count(val)
        for i in range(y):
            nums.remove(val)
            nums.append(0)
        return (len(nums)-y)