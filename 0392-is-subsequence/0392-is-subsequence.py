class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        k=0
        if len(s)==0 and len(t)==0:
            return True
        if len(s)==0:
            return True
        
        while  k<len(t):
            
            if s[i]==t[k]:
                i+=1
            k+=1
            if i==len(s):
                return True
            
        return False


            