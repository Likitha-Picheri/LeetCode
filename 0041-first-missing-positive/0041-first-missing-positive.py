class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s=set(nums)
        print(s)
        i=1
        while i in s:
            print(i)
            i+=1
        return i
        