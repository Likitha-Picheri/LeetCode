class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        x=0
        for i in range(len(jewels)):
            if jewels[i] in stones:
                x+=stones.count(jewels[i])
        return x


        