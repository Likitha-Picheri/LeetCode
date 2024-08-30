class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dict={}
        for i in range(len(t)):
            if t[i] not in dict:
                dict[t[i]]=1
            else:
                dict[t[i]]+=1
        for i in range(len(s)):
            if s[i]  in dict:
                dict[s[i]]-=1
        for key,value in dict.items():
            if value==1:
                return key
        
        

        