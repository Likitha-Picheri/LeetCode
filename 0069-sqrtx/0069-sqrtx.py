
class Solution:
    def mySqrt(self, x: int) -> int:
        number=1
        t=0
        while number*number<=x:
            t=number
            number+=1
        return t