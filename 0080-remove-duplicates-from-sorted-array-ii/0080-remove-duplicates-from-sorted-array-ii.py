class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return len(nums)
        count=0
        i=2
        while i<len(nums) and nums[i]!='-':
            if nums[i]==nums[i-2]:
                nums.remove(nums[i])
                count+=1
                nums.append('-')
            else:
                i+=1
                
            
        return len(nums)-count


        
        