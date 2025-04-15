class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        def inbound(row,col):
            return 0 <= row < len(isWater) and 0<= col < len(isWater[0])

        visited = [[False]*len(isWater[0]) for _ in range(len(isWater))]

        queue = deque()

        direction = [(0,1),(1,0),(-1,0),(0,-1)]


        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j] == 1:
                    queue.append((i,j))
                    visited[i][j] = True
                    isWater[i][j] = 0


        while queue:
            row, col = queue.popleft()

            for r , c in direction:
                new_row, new_col = row + r , col + c

                if inbound(new_row,new_col) and (not visited[new_row][new_col]):
                    isWater[new_row][new_col] = isWater[row][col] + 1
                    visited[new_row][new_col]= True
                    queue.append((new_row,new_col))


        return isWater