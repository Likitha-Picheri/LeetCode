
class Solution:
    def maximum69Number (self, num: int) -> int:
        t=num
        a=[]
        while t>0:
            a.append(t%10)
            t=t//10
        a.reverse()
        for i in range(len(a)):
            if a[i]==6:
                a[i]=9
                break
        sum=0
        for i in range(len(a)):
            sum=a[i]+sum*10
        return sum
        





        