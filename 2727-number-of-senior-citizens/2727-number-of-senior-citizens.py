class Solution:
    def countSeniors(self, details: List[str]) -> int:
        sum=0
        for t in details:
            if int(t[11:13])>60:
                sum+=1
        return sum
        