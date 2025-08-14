class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        '''
        0 0 0
        0 1 0
        1 2 1

        '''

        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        def inbound(row,col):
            return 0 <= row < len(mat) and 0 <= col < len(mat[0])
        
        visited = [[False]*len(mat[0]) for _ in range(len(mat))]

        queue = deque()

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append([i,j,0])
                    visited[i][j] = True
        
        while queue:
            for _ in range(len(queue)):
                row , col , step = queue.popleft()

                for r , c in direction:
                    new_row = row + r
                    new_col = col + c

                    if inbound(new_row,new_col) and not visited[new_row][new_col]:
                        queue.append([new_row, new_col , step + 1])
                        mat[new_row][new_col] = step + 1
                        visited[new_row][new_col] = True
        
        return mat

