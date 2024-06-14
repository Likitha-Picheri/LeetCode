class Solution:
    def isHappy(self, n: int) -> bool:
        nums=set()
        while n!=1:
            x=[int(y) for y in str(n)]
            sums=sum([z**2 for z in x])
            n=sums
            if n in nums:
                return False
            nums.add(n)
        return True

        