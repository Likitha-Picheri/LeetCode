import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        t=math.floor(math.sqrt(c))
        for i in range(t+1):
            if (math.sqrt(c-(i**2))).is_integer():
                print(math.sqrt(c-i**2))
                print(i)
                return True
            
        return False