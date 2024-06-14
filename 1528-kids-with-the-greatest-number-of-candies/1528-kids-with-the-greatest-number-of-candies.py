class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        x=[]
        t=max(candies)
        for i in range(len(candies)):
            if(candies[i]+extraCandies)<t:
                x.append(False)
            else:
                x.append(True)
        return x
        