class Solution:
    def reverseBits(self, n: int) -> int:
        binary=bin(n)
        reverse=binary[-1:1:-1]
        reverse=reverse + (32- len(reverse))*'0'
        return int(reverse,2)
        