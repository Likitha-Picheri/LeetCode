class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips=0
        while a>0 or b>0 or c>0:
            a_bits=a&1
            b_bits=b&1
            c_bits=c&1
            print(a_bits,b_bits,c_bits)
            if (a_bits | b_bits) !=c_bits:
                if c_bits==1:
                    flips+=1
                else:
                    flips+=a_bits+b_bits
            

            a>>=1
            b>>=1
            c>>=1
        return flips
