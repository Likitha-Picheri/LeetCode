class Solution:
    def reverse(self, x: int) -> int:
        r=0
        
        if x>=0:
            while x>0:
                t=x%10
                r=t+r*10
                x=x//10
            if r<=(pow(2,31)-1):
                return r
            else:
                return 0
        if x<=0:
            x=abs(x)
            while x>0:

                t=x%10
                r=t+r*10
                x=x//10
            r=-r
            if r>=-(pow(2,31)):
                return r
            else:
                return 0
        
