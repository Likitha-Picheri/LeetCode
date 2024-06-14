class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x=[]
        j=0   
        k=0 
        t=len(word1)
        m=len(word2)
        for i in range(t+m):
            if j==t and k<m:
                x.append(word2[k])
                k+=1
            elif k==m and j<t:
                x.append(word1[j])
                j+=1
            elif i%2==0 and j<t:
                x.append(word1[j])
                j+=1
            elif i%2==1 and k<m:
                x.append(word2[k])
                k+=1
        return ''.join(x)
