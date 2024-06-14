class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i=0
        j=i
        l=[]
        while i<len(nums):

            if i!=(len(nums)-1) and (nums[i]+1) != nums[i+1]:
                if i==j:
                    l.append(str(nums[i]))
                else:
                    l.append(f"{nums[j]}->{nums[i]}")
                j=i+1
            elif i==len(nums)-1:
                if nums[i]==nums[i-1]+1:
                    l.append(f"{nums[j]}->{nums[i]}")
                else:
                    l.append(str(nums[i]))
            i+=1

        return l

            