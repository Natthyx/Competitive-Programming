class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def inbound(row,col):
            return 0 <= row < len(maze) and  0 <= col < len(maze[0])

        direction = [(0,1),(1,0),(-1,0),(0,-1)]

        queue = deque()
        queue.append((entrance[0],entrance[1],0))
        maze[entrance[0]][entrance[1]]="+"
        while queue:
            row, col, step = queue.popleft()

            for r,c in direction:
                new_row , new_col = row+r, col+c
                

                if inbound(new_row,new_col) and maze[new_row][new_col] == ".":
                    if new_row == 0 or new_row == len(maze)-1 or new_col == 0 or new_col == len(maze[0])-1:
                        return step + 1 
                    
                    
                    queue.append([new_row,new_col,step+1])
                    maze[new_row][new_col]="+"
                    

        return -1