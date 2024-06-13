class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel="aeiouAEIOU"
        x=[]
        s_list=list(s)
        j=0
        for i in range(len(s)):
            if s[i] in vowel:
                x.append(s[i])
        x.reverse()
        for i in range(len(s)):
            if s[i] in vowel:
                s_list[i]=x[j]
                j+=1
        return "".join(s_list)
        