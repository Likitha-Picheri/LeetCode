
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<1:
            return False
        elif n==1 or n==3:
            return True
        else:
            for i in range(n//3):
                t=3**i
                if t==n:
                    return True
                if t>n:
                    return False
                

        