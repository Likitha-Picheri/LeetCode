class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if n==k:
            return 0
        count=0
        while n>0:
            k_bit=k&1
            n_bit=n&1
            if k_bit!=n_bit and n_bit!=1:
                
                return -1
            elif k_bit!=n_bit and n_bit==1:
                count+=1
            k>>=1
            n>>=1
        return count if k==0 else -1

                   

        