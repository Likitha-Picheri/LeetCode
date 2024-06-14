class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x=[0]*(2*n)
        j=0
        for i in range(n):
            x[j]=nums[i]
            x[j+1]=nums[i+n]
            j+=2
        return x


        