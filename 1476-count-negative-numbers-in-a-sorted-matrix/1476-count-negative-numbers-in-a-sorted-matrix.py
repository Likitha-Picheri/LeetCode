class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c=0
        t=len(grid)
        for i in range(t):
            for j in range(len(grid[i])):
                if grid[i][j]<0:
                    c+=1
        return c
        