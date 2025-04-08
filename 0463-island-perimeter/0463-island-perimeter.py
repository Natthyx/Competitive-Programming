class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        store = []
        def inbound(row,col):
            return ( 0 <= row < len(grid) and (0 <= col < len(grid[0])))
        def dfs(row,col):

            if grid[row][col] == 1:
                store.append([row,col])

            visited[row][col] = True

            for r , c in direction:
                new_row = row + r
                new_col = col + c

                if inbound(new_row,new_col) and not visited[new_row][new_col]:
                    dfs(new_row,new_col)

        dfs(0,0)
        ans = 0
        for row, col in store:
            for r , c in direction:
                new_row = row + r
                new_col = col + c
                if not inbound(new_row,new_col):
                    ans+=1
                elif inbound(new_row,new_col) and grid[new_row][new_col]==0:
                    ans+=1
        return ans
        
        






        

        

