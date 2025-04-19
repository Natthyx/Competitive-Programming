class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        direction = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]

        def inbound(row,col):
            return  0 <= row < len(board) and 0 <= col < len(board[0])

        visited = [[False]*len(board[0]) for _ in range(len(board))]

        queue = deque()
        rw , cl = click
        if board[rw][cl] == "M":
            board[rw][cl] = "X"
            return board

        queue.append((rw,cl))


        while queue:
            row , col = queue.popleft()
            visited[row][col] = True
            neighbor = []
            count = 0
            for r, c in direction:
                nr, nc = row + r , col + c
                
                if inbound(nr,nc) and (not visited[nr][nc]) and board[nr][nc] == "M":
                    count += 1
                elif inbound(nr,nc) and (not visited[nr][nc]) and board[nr][nc] == "E":
                    neighbor.append((nr,nc))
            if count > 0:
                board[row][col] = str(count)
            else:
                board[row][col] = "B"
                for nr , nc in neighbor:
                    queue.append((nr,nc))
                    visited[nr][nc]=True
        
        return board
                
