class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def targets(List,target,high,low):
            if high>=low:
                mid=(high+low)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]>target:
                    return targets(nums,target,mid-1,low)
                else:
                    return targets(nums,target,high,mid+1)
            else:
                return -1
        n=len(nums)-1
        return targets(nums,target,n,0)



        