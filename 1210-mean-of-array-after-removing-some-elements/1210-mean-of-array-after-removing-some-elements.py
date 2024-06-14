class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        t=len(arr)
        l=0.05*t
        l=int(l)
        for i in range(l):
            arr.remove(min(arr))
            y=-1-i
            arr.remove(max(arr))
        y=sum(arr)
        return y/len(arr)