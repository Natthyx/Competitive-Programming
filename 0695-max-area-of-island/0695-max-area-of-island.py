class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        direction = [(0,1),(1,0),(-1,0),(0,-1)]

        def inbound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[row])

        visited = set()
        colored = 0
        ans = 0

        def dfs(row,col):
            nonlocal colored

            colored += 1
            visited.add((row,col))

            for r, c in direction:
                new_row = row + r
                new_col = col + c

                if inbound(new_row,new_col) and (new_row,new_col) not in visited:
                    if grid[new_row][new_col] == 1:
                        dfs(new_row,new_col)
            
            


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    dfs(i,j)
                    ans = max(ans,colored)
                    colored = 0

        return ans


        