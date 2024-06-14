class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        t=len(arr)//4
        for i in set(arr):
            if arr.count(i) >t:
                return i