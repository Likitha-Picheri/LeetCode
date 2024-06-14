class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left,right = 0,n 
        l_sum,r_sum = 0,sum(nums)
        output = []
        for i in range(n):
            output.append(left*nums[i]-l_sum+r_sum-right*nums[i])
            left+=1 
            right-=1
            l_sum +=nums[i]
            r_sum -=nums[i]
        return output
        