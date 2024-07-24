class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        final_pascal=[]
        final_pascal.append([1])
        for i in range(numRows-1):
            new=[1]
            for j in range(i):
                new.append(final_pascal[i][j]+final_pascal[i][j+1])
            new.append(1)
            final_pascal.append(new)
        return final_pascal
        