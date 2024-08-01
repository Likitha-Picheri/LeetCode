class Solution:
    def countSeniors(self, details: List[str]) -> int:
        sum=0
        for t in details:
            x=t[11]+t[12]
            print(x)
            if x>'60':
                sum+=1
        return sum
        