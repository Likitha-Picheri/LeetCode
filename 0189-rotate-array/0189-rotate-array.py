class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
       
        t=0
        while t!=k:
            nums.insert(0,nums.pop())
            t+=1

        