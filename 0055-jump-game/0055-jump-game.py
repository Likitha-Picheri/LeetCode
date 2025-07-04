class Solution:
    def canJump(self, nums: List[int]) -> bool:
        step=0
        for i in range(len(nums)-1):
            
            if step<nums[i]:
                step=nums[i]
            step-=1
            if step<0:
                return False
        if step>=0:
            return True
        else:
            return False
        
        
        