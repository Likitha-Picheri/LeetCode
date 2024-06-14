class Solution:
    def pivotInteger(self, n: int) -> int:
        if n==1:
            return 1
        elif n>1 and n<=7:
            return -1
        else:
            t=(n*(n+1))//2
            for i in range(3,n-1):
                if ((i*(i+1))//2)==(t-((i-1)*(i))//2):
                    return i
        return -1
        