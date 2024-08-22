class Solution:
    def findComplement(self, num: int) -> int:
        t=bin(num).replace("0b","")
        num_1=(1<<len(t))-1

        return int(t,2)^num_1

        