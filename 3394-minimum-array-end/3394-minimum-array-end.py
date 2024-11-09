class Solution:
    def minEnd(self, n: int, x: int) -> int:
        if n == 1:
            return x

        nth = bin(n - 1)[2:]  # Binary representation of (n - 1)
        mask = bin(x)[2:]      # Binary representation of x

        result = ""
        right = len(nth) - 1

        # Process mask from right to left
        for i in range(len(mask) - 1, -1, -1):
            if mask[i] == '1':
                result = '1' + result
            else:
                result = (nth[right] if right >= 0 else '0') + result
                right -= 1

        # Append remaining bits of nth
        while right >= 0:
            result = nth[right] + result
            right -= 1

        return int(result, 2)
        