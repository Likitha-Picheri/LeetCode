class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        i=0
        j=0
        count=0
        while i<len(g) and j<len(s):
            if g[i]<=s[j]:
                i+=1
                j+=1
                count+=1
            elif g[i]>s[j]:
                i+=1
                
        return count



        