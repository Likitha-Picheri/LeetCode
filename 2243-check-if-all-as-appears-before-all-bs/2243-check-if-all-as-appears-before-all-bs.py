class Solution:
    def checkString(self, s: str) -> bool:
        booll=0
        for i  in range(len(s)):
            if(s[i]=='b'):
                booll=1
            if booll==1 and s[i]=='a':
                return False
        return True

        