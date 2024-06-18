class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        sum1=(n*(n+1))//2
        t=sum(list(set(nums)))
        return (sum(nums)-t,sum1-t)

        