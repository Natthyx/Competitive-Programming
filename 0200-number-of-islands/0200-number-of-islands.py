class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        row , col = len(grid) , len(grid[0])

        def inbound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        queue = deque()
        visited = [[False]*col for _ in range(row)]

        def dfs(row,col):
            visited[row][col] = True

            for r , c in direction:
                new_row, new_col = row+r , col + c

                if inbound(new_row,new_col) and grid[new_row][new_col] == "1" and not visited[new_row][new_col]:
                    dfs(new_row,new_col)


        count = 0
        for i in range(row):
            for j in range(col):
                if not visited[i][j] and grid[i][j] == "1":
                    count +=1
                    dfs(i,j)
        
        return count