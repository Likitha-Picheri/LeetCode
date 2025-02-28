class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        sum1=0
        maximum=0
        for i in range(len(nums)):
            if i==len(nums)-1:
                sum1+=nums[i]
                return max(maximum,sum1)
            elif  nums[i]>nums[i+1] or nums[i]==nums[i+1]:
                sum1+=nums[i]
                maximum=max(sum1,maximum)
                print(maximum)
                sum1=0
            else:
                sum1+=nums[i]
                print(nums[i])
            

        return max(sum1,maximum)
            
        