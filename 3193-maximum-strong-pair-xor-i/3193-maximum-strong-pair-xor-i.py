class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
       
        left=0
        right=1
        max=0
        y=len(nums)
        while(left<(y -1)):
            if right==len(nums):
                left+=1
                right=left+1
            if (left<y-1 and right<y):
                if (abs(nums[left]-nums[right])<=min(nums[left],nums[right]))    :
                    z=nums[left]^nums[right]
                    if max<=z:
                        max=z   
           
            right+=1
        return max


        