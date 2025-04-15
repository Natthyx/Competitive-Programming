class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def inbound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        queue = deque()
        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    fresh+=1
 
        time = 0
        while queue and fresh > 0:
            for _ in range(len(queue)):
                row , col = queue.popleft()

                for r , c in direction:
                    new_row , new_col = row + r , col + c
                    
                    if inbound(new_row,new_col) and grid[new_row][new_col] == 1:
                        queue.append((new_row,new_col))
                        grid[new_row][new_col]=2
                        fresh-=1
            
            time += 1

        return time if fresh == 0 else -1