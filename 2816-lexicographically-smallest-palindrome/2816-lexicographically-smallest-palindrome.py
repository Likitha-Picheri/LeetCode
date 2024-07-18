class Solution(object):
    def makeSmallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        left=0
        right=len(s)-1
        s=list(s)
        while(left<=right):
            if(s[left]>s[right]):
                s[left]=s[right]
            elif(s[right]>s[left]):
                s[right]=s[left]
            left+=1
            right-=1
        return ''.join(s)


        