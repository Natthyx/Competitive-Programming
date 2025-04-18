class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row , col = len(mat), len(mat[0])

        def inbound(row,col):
            return 0 <= row < len(mat) and 0 <= col < len(mat[0])

        direction = [(0,1),(1,0),(-1,0),(0,-1)]

        visited = [[False] * col for _ in range(row)]

        queue = deque()

        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    queue.append((i,j,0))
                    visited[i][j] = True

        while queue:
            roww, coll , step = queue.popleft()

            for r, c in direction:
                new_row , new_col = roww + r , coll + c
                if inbound(new_row,new_col) and (not visited[new_row][new_col]):
                    visited[new_row][new_col] = True
                    mat[new_row][new_col] = step + 1
                    queue.append((new_row,new_col,step+1)) 
                    

        return mat
