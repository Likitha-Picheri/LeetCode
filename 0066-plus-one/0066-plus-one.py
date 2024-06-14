class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        t=len(digits)-1
        l=len(digits)
        r=0
        y=0
        while t>=0:
            r=r+digits[y]*pow(10,t)
            y=y+1
            t=t-1
        r=r+1
        k=0
        while r>0:
            j=r%10
            r=r//10
            if k<l:
                digits[k]=j
            else:
                digits.append(j)
            k+=1
        digits.reverse()
        return digits

        