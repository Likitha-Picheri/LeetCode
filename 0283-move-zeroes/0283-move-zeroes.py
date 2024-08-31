class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i=len(nums)-1
        while i>=0:
            print(nums[i])
            if nums[i]==0:
            
                nums.append(nums.pop(i))
            i-=1
        return nums
