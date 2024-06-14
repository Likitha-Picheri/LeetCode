class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        t=min(nums)
        m=max(nums)
        lists=[]
        for i in nums:
            c=0
            for j in range(len(nums)):
                if i>nums[j]:
                    c+=1
            lists.append(c)
        return lists
        