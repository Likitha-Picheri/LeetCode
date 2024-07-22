class Solution:
    def isPalindrome(self, x: int) -> bool:
        t=str(x)
        left=0
        right=len(t)-1
        while(left<=right):
            if t[left]!=t[right]:
                return False
            left+=1
            right-=1
        return True
            # rev = 0
            # init_n = x
            # if( x < 0):
            #   return False
            # while x != 0:
            #         rev = (rev*10) +  x % 10
            #         x = x // 10
    
            # if(rev == init_n):
            #            return True
            # return False
