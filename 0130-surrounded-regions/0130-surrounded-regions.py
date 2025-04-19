class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def inbound(row,col):
            return 0 <= row < len(board) and  0 <= col < len(board[0])
        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = [[False]*len(board[0]) for _ in range(len(board))]
        
        def dfs(row,col,flag,component):
            visited[row][col] = True
            component.append((row,col))

            if row == 0 or row == len(board)-1 or col == 0 or col == len(board[0])-1:
                flag[0]=False
            
            for r , c in direction:
                nr , nc = row + r , col + c

                if inbound(nr,nc) and board[nr][nc] == "O" and not visited[nr][nc]:
                        dfs(nr,nc,flag,component)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if not visited[i][j] and board[i][j] == "O":
                    component = []
                    flag = [True] 
                    dfs(i,j,flag,component)
                    if flag[0]:
                        for r,c in component:
                            board[r][c] = "X"    
