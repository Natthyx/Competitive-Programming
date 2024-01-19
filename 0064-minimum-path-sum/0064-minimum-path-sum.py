class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows , cols  = len(grid) , len(grid[0])
        
        res = [[float("inf")]  * (cols +1) for row in range(rows + 1)]
        res[rows-1][cols] = 0
        
        for row in range(rows-1,-1,-1):
            for col in range(cols-1,-1,-1):
                res[row][col] = grid[row][col] + min(res[row+1][col], res[row][col+1])
        return res[0][0]
                
        