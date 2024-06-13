class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        if not s:
            return 0
        i=0
        sum=0
        sign=1
        if s[i]=="+":
            i+=1
        elif s[i]=="-":
            i+=1
            sign=-1
        while i<len(s) and s[i].isdigit():
            sum=sum*10+ int(s[i])
            i+=1
        sum *=sign
        sum=max(min(sum,2**31 -1), -2**31)
        return sum