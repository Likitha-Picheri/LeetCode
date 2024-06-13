class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        list1=[]
        nums.sort()
        i=0
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                sum1=nums[i]+nums[j]+nums[k]
                if sum1>0:
                    k-=1
                elif sum1<0:
                    j+=1
                
                else:
                    list1.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
        return list1