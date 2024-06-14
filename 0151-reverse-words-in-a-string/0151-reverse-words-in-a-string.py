class Solution:
    def reverseWords(self, s: str) -> str:
        y=s.split()
        t=y[::-1]
        return str(" ".join(t))

        