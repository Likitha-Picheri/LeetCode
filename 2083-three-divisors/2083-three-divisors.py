class Solution:
    def isThree(self, n: int) -> bool:
        t=0
        if n<=3:
            return False
        else:
            for i in range(2,(n//2)+1):
                if n%i==0:
                    t+=1
                if t>1:
                    return False

        if t==1:
            return True
        else:
            return False

        