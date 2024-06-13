class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        t=heights[:]
        t.sort(reverse=True)
        z=[]
        for i in range(len(names)):
            index1=heights.index(t[i])
            z.append(names[index1])
        return z
        
        