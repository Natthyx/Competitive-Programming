class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        def inbound(row,col):
            return 0 <= row < len(image) and 0 <= col < len(image[0])

        
        queue = deque()
        queue.append((sr,sc))
        visited = [[False]*len(image[0]) for _ in range(len(image))]
        first = image[sr][sc]
        image[sr][sc] = color

        while queue:
            row ,col = queue.popleft()
            visited[row][col] = True
            

            for r , c in direction:
                new_row , new_col = row + r , col + c

                if inbound(new_row,new_col) and (not visited[new_row][new_col]) and image[new_row][new_col] == first:
                    image[new_row][new_col]=color
                    visited[new_row][new_col] = True
                    queue.append((new_row,new_col))

        return image


