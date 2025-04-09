class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction = [(0,1),(1,0),(-1,0),(0,-1)]

        def inbound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) 

        visited = set()

        def dfs(row,col):
            
            visited.add((row,col))

            for r , c in direction:
                new_row = row + r
                new_col = col + c

                if inbound(new_row,new_col) and (new_row,new_col) not in visited:
                    if grid[new_row][new_col] == "1":
                        dfs(new_row,new_col)
        ans = 0     
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    ans += 1
                    dfs(i,j)


        return ans



