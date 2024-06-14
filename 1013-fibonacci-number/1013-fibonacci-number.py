class Solution:
    def fib(self, n: int) -> int:
        x=[]
        x.append(0)
        x.append(1)
        for i in range(2,n+1):
            x.append(x[i-1]+x[i-2])
        return x[n]
    
        