class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance=0
        while x>0 or y>0:
            a=x&1
            b=y&1
            if (a!=b):
                print(a,b)
                distance+=1
            x>>=1
            y>>=1
        return distance
        