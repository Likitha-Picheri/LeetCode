class Solution:
    def getSum(self, a: int, b: int) -> int:
        masks=0xffffffff
        
        while(b&masks)>0:
            c=a&b
            a=a^b
            b=c<<1
        return (a&masks)  if b>0 else a
        