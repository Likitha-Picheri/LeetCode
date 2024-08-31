class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        n=len(s)
        if n%2!=0:
            return False
        for i  in range(n):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                a.append(s[i])
            else:
                if (s[i]==']' or s[i]==')' or s[i]=='}') and len(a)==0:
                    return False
                elif s[i]==']' and a[-1]=='[':
                    a.pop()
                elif s[i]==')' and a[-1]=='(':
                    a.pop()
                elif s[i]=='}' and a[-1]=='{':
                    a.pop()
                elif s[i]==']' and a[-1]!='[' or s[i]==')' and a[-1]!='(' or s[i]=='}' and a[-1]!='{':
                    return False
                
        if len(a)==0:
            return True
        else:
            return False
            
            
        