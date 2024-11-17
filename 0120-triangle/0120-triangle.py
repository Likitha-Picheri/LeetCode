class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        for i in range(1,n):
            triangle[i][0]+=triangle[i-1][0]
            triangle[i][-1] += triangle[i-1][-1]
            for j in range(1,len(triangle[i])-1):
                triangle[i][j] += min(triangle[i-1][j-1],triangle[i-1][j])
        return min(triangle[-1])
        
        # sum1=triangle[0][0]
        # if len(triangle)==1:
        #     return sum1
        # k=0
        # for i in range(1,len(triangle)-1):
        #     min1=float('inf')
        #     k=0
        #     for j in range(len(triangle[i])):
        #         temp=min(triangle[i][j]+triangle[i+1][j],triangle[i][j]+triangle[i+1][j+1])
        #         if temp<min1:
        #             k=j
        #             min1=temp
        #     print(triangle[i][k])
        #     sum1+=triangle[i][k]
        # sum1+=min(triangle[-1][k],triangle[-1][k+1])
        # return sum1
                

            
        
        